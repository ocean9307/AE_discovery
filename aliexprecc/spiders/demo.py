import re
tar_a = '//www.aliexpress.com/item/Cupshe-Wish-You-Well-Lace-One-piece-Swimsuit-Cutout-Deep-V-neck-Sexy-Bodysuit-Bikini-Set/32850467287.html?ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_10151_10344_10068_10342_10325_10343_10546_10340_10059_10341_10548_10696_100031_10084_10083_10103_10618_10307_10624_10623_10622_10621_10620,searchweb201603_25,ppcSwitch_5&algo_expid=0ae71e0c-366e-420e-a34e-f7017cd996b1-0&algo_pvid=0ae71e0c-366e-420e-a34e-f7017cd996b1&priceBeautifyAB=0'
# a_url = re.findall('(\d*?).html', tar_a)[0] #a标签里的url
a_url = re.search('www(.*?)html', tar_a).group()
print(a_url)
print(dir(a_url))
# print(a_url.group())