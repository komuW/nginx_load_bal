# Nginx load balancer


This is an example of how you can use nginx as a load balancer.


# setup    
* you'll need to have ansible and vagrant already installed:   
* clone this repository
* change directory in this repository's directory
* vagrant up
* go to `localhost:4700` on your host machine


# explanation
* as part of the setup, an nginx conf file will be created inside the virtual machine at /etc/nginx/sites-enabled/django_app
* this conf file will have in it the three different nginx load balancing methods:        
     - round robin        
     - least connected         
     - ip-hash

* by default a small django app will also be created and it will be listening on both port 3000 and 4500 in the guest OS. 
* nginx will act as proxy/load balancer listening on port 4700 in the guest(which is also forwarded to port 4700 in the host OS)
* nginx will route requests to the two appliaction instances (listening on port 3000 and 4500) in a round robbin manner.
* if you want to change the load balancing method; edit the file /project_dir/devops/templates/app_ninx.site.conf.j2, specifically the line:           
`proxy_pass http://myapp_round_robbin_example;`          
change that to any other load balancing method listed therein, eg;           
`proxy_pass http://myapp_ip_hash_example;`           
Then run, `vagrant provision` for the changes to take effect. 



komuw05 @ gmail . com
