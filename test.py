string = '''
<strong><img src="./img-apple-64/1f4b3.png" class="emoji emoji-small" alt="💳" data-path="./img-apple-64/1f4b3.png">&nbsp;Купить криптовалюту: TON за RUB</strong><br><br><strong>Покупка:</strong>&nbsp;270.812698852 TON за 25'000 RUB<span class="MessageMeta" dir="ltr"><span class="message-time">19:18</span></span>
'''

array = string.split("data-path=")

print(array[1])