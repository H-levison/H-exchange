let rates = {};

// Load the exchange rates from the JSON file
async function loadRates() {
    try {
        const response = await fetch('./exchange_rates.json');
        rates = await response.json();

        // Update the page with the rates
        document.getElementById('usdRwf').textContent = `USD/RWF: ${rates['USD/RWF']}`;
        document.getElementById('ngnRwf').textContent = `NGN/RWF: ${rates['NGN/RWF']}`;
        document.getElementById('usdNgn').textContent = `USD/NGN: ${rates['USD/NGN']}`;
    } catch (error) {
        console.error('Error loading rates:', error);
    }
}

// Convert currency based on the rates
function convertCurrency() {
    const amount = parseFloat(document.getElementById('amount').value);
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;
    const resultElement = document.getElementById('result');

    if (!amount) {
        resultElement.textContent = 'Please enter an amount';
        return;
    }

    if (Object.keys(rates).length === 0) {
        resultElement.textContent = 'Rates are not loaded yet, please try again.';
        return;
    }
    
    const rateKey = `${fromCurrency}/${toCurrency}`;
    let rate;

    if (fromCurrency === toCurrency) {
        rate = 1;
    } else if (rates[rateKey]) {
        rate = rates[rateKey];
    } else {
        const inverseKey = `${toCurrency}/${fromCurrency}`;
        rate = 1 / rates[inverseKey];
    }

    const result = amount * rate;
    resultElement.textContent = `${amount} ${fromCurrency} = ${result.toFixed(2)} ${toCurrency}`;
}

// Swap currencies
function swapCurrencies() {
    const fromSelect = document.getElementById('fromCurrency');
    const toSelect = document.getElementById('toCurrency');
    const temp = fromSelect.value;
    
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
    
    // Clear the result when swapping
    document.getElementById('result').textContent = '';
}

// Initialize on page load
window.onload = function() {
    loadRates();
};
