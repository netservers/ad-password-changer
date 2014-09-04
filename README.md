ad-password-changer
===================

Active Directory password change. 

requirements
============

python >= 2.7

samba

installation
============

DEB:
    apt-get install nginx supervisor

RPM:
    yum install nginx supervisor

    chkconfig supervisord on
    chkconfig nginx on
    cd /opt
    git clone https://github.com/ribeiroit/ad-password-changer.git
    cd ad-password-changer
    mkdir env && virtualenv env
    ./env/bin/pip install -r requirements.txt
    cp config.sample.py config.py


    cat utils/supervisord.conf >> /etc/supervisord.conf
    cp utils/ad-password-changer.nginx.conf /etc/nginx/conf.d/
    sed -i bak -e /YOUR_DOMAIN/<put_your_domain_here>/g /etc/nginx/conf.d/ad-password-changer.nginx.conf
    service supervisord restart
    service nginx restart