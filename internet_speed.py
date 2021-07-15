import speedtest
speed = speedtest.Speedtest()

print("Test Download Speed")
# دریافت سرعت بر حسب بیت و تبدیل به مگابایت
download_result = speed.download()/1024/1024
print("Your download speed is: {} mbit/s".format(download_result))

print("Test Upload Speed")
upload_result = speed.upload()/1024/1024

#نمایش سرعت اینترنت بر حسب مگابایت 
print("Your upload speed is: {} mbit/s".format(upload_result))


print("Test Ping Test")
ping_result = speed.results.ping
print("Your ping speed is: {} ms".format(ping_result))
