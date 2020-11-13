import glob
import time
import pandas as pd
import requests

payload = {}
headers = {
  'Authorization': 'OAuth oauth_consumer_key="xxx",oauth_token="xx-xxx",oauth_signature_method="xx-xx",oauth_timestamp="xx",oauth_nonce="xx",oauth_version="1.0",oauth_signature="xxx"',
  'Cookie': 'personalization_id="xx"; guest_id=xx'
}

for file in glob.glob('./datasets/filteredchunks/*.csv'):
	df = pd.read_csv(file, sep=',', usecols=['tweet_id'])
	# tiap line di df nya dijadiin string trus ditambahin koma trus disambung line berikutnya
	# trus dimasukin ke url nanti jadi "...?ids=932579209434,9830278237,932798721074,dst..."
	url = "https://api.twitter.com/2/tweets?ids="
    # gimana caranya nambahin string ke url?
	response = requests.request("GET", url, headers=headers, data = payload)
	ini pinginnya ga diprint tapi disimpen ke json atau csv gitu buat nanti dineural network enaknya gimana ya mas?
    # print(response.text.encode('utf8'))
    time.sleep(300)
