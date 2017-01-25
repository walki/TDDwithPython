Provisioning a new site
=======================
## Required Packages:
* nginx
* Python 3
* Git
* pip
* virtualenv
* gunicorn
* systemd  (not Upstart)


e.g. on Ubuntu:
  sudo apt-get install nginx python3 python3-pip
  sudo pip3 install virtualenv
  sudo pip3 install gunicorn


## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with e.g., staging.my-domain.com

## Systemd Job
* see gunicorn.systemd.template.conf
* replace SITENAME with e.g., staging.my-domain.com

## Folder Structure:
Assume we have a user account at /home/username

/home/username
├── sites
│   └── SITENAME
│       ├── database
│       ├── source
│       ├── static
│       └── virtualenv


// Adding the new site to the available and enabled sites lists
sed "s/SITENAME/superlists.backuptheb.us/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/superlists.backuptheb.us
sudo ln -s ../sites-available/superlists.backuptheb.us /etc/nginx/sites-enabled/superlists.backuptheb.us
// Adding the systemd start up script
sed "s/SITENAME/superlists.backuptheb.us/g" deploy_tools/gunicorn-systemd.template.conf | sudo tee /etc/systemd/system/gunicorn.superlists.backuptheb.us.service
// Start the new Service
sudo service nginx reload
sudo systemctl start gunicorn.superlists.backuptheb.us.service
