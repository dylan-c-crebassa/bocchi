# Check if Python 3.13+ is installed
if (-not (Get-Command "py.exe" -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed or not available in PATH." -ForegroundColor Red
    exit 1
}

# Create a virtual environment
Write-Host "Creating virtual environment..."
py.exe -m venv .venv



# Install dependencies
Write-Host "Installing requirements..."
if (-Not (Test-Path requirements.txt)) {
    Write-Host "Error: requirements.txt not found in the current directory!" -ForegroundColor Red
    exit 1
}
py.exe -m pip install -r requirements.txt

Write-Host "Activating virtual environment..."
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

Write-Host "Environment setup completed successfully." -ForegroundColor Green
