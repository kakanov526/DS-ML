pandas
numpy
matplotlib
seaborn
scipy
streamlit

!pip install -r requirements.txt -q
!pip install pyngrok -q

from pyngrok import ngrok

# Terminate ngrok tunnels if any are already running
ngrok.kill()

# Authenticate ngrok. This assumes you have an ngrok authtoken.
# Replace 'YOUR_NGROK_AUTHTOKEN' with your actual authtoken.
# You can get one from https://dashboard.ngrok.com/get-started/your-authtoken
# ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN") 

public_url = ngrok.connect(addr='8501', proto='http')
print(f'Tunnel URL: {public_url}')

!streamlit run clean_app.py
