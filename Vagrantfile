#!/usr/bin/env ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "precise32"

  config.vm.box_url = "http://files.vagrantup.com/precise32.box"
  
  # django_app
  config.vm.network :forwarded_port, guest: 4700, host: 4700,
    auto_correct: true

  config.ssh.forward_agent = true
  
  # Share devops folder with guest VM. 
  config.vm.synced_folder './devops', '/vagrant/devops', 
      :mount_options => ['fmode=666']

  # shell provisioning
  config.vm.provision :shell, :path => "devops/dev_provision.sh"

end
