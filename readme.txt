# Simple repo to use pywinrm to talk with Windows instance

Create/use python virtual environment:

    virtualenv -p python3 venv
    source venv/bin/activate

Install python libs:

    pip install pypsrp

Optionally, install direnv and run:

    direnv allow

Assuming you have VirtualBox or VMware Fusion and/or Workstation installed,
optionally, install mikemech:

    pip install mikemech
    mech init StefanScherer/windows_10
    mech up

Try out example:

    ./example_dir.py 192.168.3.135
    ./ps.py 192.168.3.135 'Write-Output hello'
    ./ps_using_winrs.py 192.168.3.135 "powershell Write-Host hello"
