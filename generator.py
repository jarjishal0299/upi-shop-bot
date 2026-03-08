import qrcode
import json
import os

def generate_upi_qr(upi_id, amount, file_name):
    # Data to generate QR code
    upi_data = f'UPI:{upi_id}?amount={amount}&pa={upi_id}&pn=MerchantName&mc=1234&tid=2026-03-08 09:17:11&tid=2026-03-08 09:17:11&tn=Payment&am={amount}&cu=INR&url=https://example.com'
    
    # Generate QR code
    qr_code = qrcode.make(upi_data)
    
    # Save the generated QR code to a file
    qr_code.save(file_name)
    
    # Store data in a file
    log_data = {
        'upi_id': upi_id,
        'amount': amount,
        'file_name': file_name,
        'timestamp': '2026-03-08 09:17:11'
    }
    
    # Save log data to JSON file
    if not os.path.exists('logs'):
        os.makedirs('logs')
    log_file_path = os.path.join('logs', 'upi_data_log.json')
    
    # Append new log entry to the existing log file
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r+') as log_file:
            data = json.load(log_file)
            data.append(log_data)
            log_file.seek(0)
            json.dump(data, log_file, indent=4)
    else:
        with open(log_file_path, 'w') as log_file:
            json.dump([log_data], log_file, indent=4)

# Example usage
if __name__ == '__main__':
    generate_upi_qr('example@upi', 100.00, 'upi_qr_code.png')