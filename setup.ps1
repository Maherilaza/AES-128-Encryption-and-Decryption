$python = Get-Command python3
if ($python -eq $null) {
    Start-BitsTransfer -Source "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe" -Destination "C:\python-3.10.0-amd64.exe"
    Start-Process -FilePath "C:\python-3.10.0-amd64.exe" -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait
}

$pip = Get-Command pip
if ($pip -eq $null) {
    Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
    python get-pip.py
}

pip install -r requirements.txt

$answer = Read-Host "Do you want to encrypt a file? (y/n)"
if ($answer -eq "y") {
    python encrypt.py
} else {
    Write-Host "Exiting after installation"
}
