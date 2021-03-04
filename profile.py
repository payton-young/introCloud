import geni.portal as portal
import geni.rspec.pg as rspec

#Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
#Create a XenVM

node = request.XenVM("node")
kubenode = request.XenVM("kubenode")
ldapnode = request.XenVM("ldapnode")
sqlsnode = request.XenVM("sqlsnode")

node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

kubenode.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
kubenode.routable_control_ip = "true"

ldapnode.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
ldapnode.routable_control_ip = "true"

sqlsnode.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
sqlsnode.routable_control_ip = "true"



node.addService(rspec.Execute(shell="/bin/sh",
                                    command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh",
                                    command="sudo apt install mysql-server"))
node.addService(rspec.Execute(shell="/bin/sh",
                                     command='sudo mysql_secure_installation -y'))

#Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
