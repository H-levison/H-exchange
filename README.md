
## *H-Exchange*
H-Exchange is a seamless currency converter web application that provides real-time exchange rates for USD, NGN, and RWF. The platform allows users to quickly check conversion between these currencies while also displaying live exchange rate updates.

## Demo
Link to Webapp: [H-exchange](https://exchange.honourgod.tech/)
Link to Demo Video: [Watch the demo on YouTube](https://youtu.be/xDoMSmrQ1d4)
  
## Features
- Real-time currency conversion
- Swapping functionality between selected currencies
- Live exchange rate ticker
- Direct link for users to initiate transactions via WhatsApp.
- Optimized UI for both desktop and mobile devices

## Technologies Used
- HTML, CSS, JavaScript (Frontend)
- Python (Backend for fetching exchange rates)
- JSON (Data storage for exchange rates)
- Nginx (Web server)
- HAProxy (Load balancer)
# Setup the Environment
1. **SSH into your web_servers**

> ssh "web server ip"

 2. **Ensure you have Python installed**
> python --version
 

## Clone the Repository
Clone the repository in this path `/var/www/`

>     cd /var/www/
>     git clone https://github.com/H-levison/H-exchange.git

## Deployment
The application is deployed on multiple servers with a load balancer to distribute traffic. *Below are the deployment steps:*
1.  **Install Dependencies**: On both web servers, install Nginx:
>     sudo apt update
>     sudo apt install nginx
*The web application is hosted on two web servers (web-01 and web-02). Nginx is used to serve the frontend and backend scripts. The exchange rate API script runs on a cron job to update exchange rates every 24 hours*

2. **Configure Nginx**
- On each web server, configure Nginx to serve the application:
Edit the Nginx configuration file  `(/etc/nginx/sites-available/default)`

   
        
    
    	server { 
	    	listen 80;
	    	server_name exchange.honourgod.tech;
	    	root /var/www/H-exchange;
	    	index index.html;
    	 
	    	location / {
	    		try_files $uri $uri/ =404;
        	}
       }

- Reload Nginx:

 

    

> `sudo systemctl restart nginx`

  

3. **Setup HAProxy as Load Balancer**

  

On the load balancer server (lb-01), configure HAProxy to distribute traffic between web-01 and web-02.
-   **Install Dependencies**: On load balancer servers, install Haproxy:
>     sudo apt update -y
>     sudo apt install haproxy

    Edit /etc/haproxy/haproxy.cfg:

> defaults
> mode http
> timeout connect 5000ms
> timeout client 50000ms
> timeout server 50000ms
>   
> 
> frontend http_front
	> bind *:80
	>default_backend web_servers
> 
> backend web_servers
> balance roundrobin
> server web1 "web01 IP>:80 check
> server web2 "web02 IP":80 check

  

Restart HAProxy:

    sudo systemctl restart haproxy

## Testing the app

- Ensure you save your api key to a `.env` file
**⚠️ Important:** Do not commit your `.env` file to GitHub. Store API keys securely using `.gitignore`.
- Run the python file to update exchange rates to `exchange_rates.json`

> cd /var/www/ 
> python3 `exchange.py` file


## Updating the Application

  

To pull the latest changes from GitHub:

    cd /var/www/H-exchange
    git pull origin main

  

## Cron Job for Updating Exchange Rates

  

A cron job is set up to fetch the latest exchange rates and update the exchange_rates.json file every 24 hours.


Edit the crontab with:

    crontab -e
Add the following line to run the script every 24 hours:

  

    0 0 * * * /usr/bin/python3 /var/www/H-exchange/exchange.py

  

## API Credits

  

H-Exchange uses [ExchangeAPI](https://app.exchangerate-api.com/) to fetch real-time currency exchange rates.
[ExchangeAPI Documentation](https://www.exchangerate-api.com/docs/overview)

  
## Note
/*This software was built to be used by Nigerians living in Rwanda and Rwandans living in Nigeria*/

## Contributing

  

Feel free to fork the repo, create a feature branch, and submit a pull request!
