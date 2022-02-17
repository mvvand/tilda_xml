import xmltodict
import json

offer1 = """<offer id="55709" type="vendor.model" available="true">
<url>https://glem.com.ua/zhenskie-platya-optom-bolshie-razmeri/0301-plate-rubashka-bordo.html</url>
<price>845</price>
<currencyId>UAH</currencyId>
<sale>0</sale>
<categoryId>26616</categoryId>
<avail quantity="0">
<size quantity="1">58</size>
<size quantity="1">50</size>
<size quantity="1">54</size>
</avail>
<picture>https://glem.com.ua/ii/images/23fdc51d4a380d20e5764bfe70f5ce9b.jpg</picture>
<picture>https://glem.com.ua/ii/images/70288b01d746e7edb81b7f6857674ea0.jpg</picture>
<picture>https://glem.com.ua/ii/images/7a4dcdf37eba07ba9359bfbde3ab538b.jpg</picture>
<picture>https://glem.com.ua/ii/images/002cc5491ebf744ce63948f481e97913.jpg</picture>
<picture>https://glem.com.ua/ii/images/26a58dbd66190607d33e67b95a529b58.jpg</picture>
<picture>https://glem.com.ua/ii/images/8c1e2251410a9fc9c54eab509211857f.jpg</picture>
<store>true</store>
<delivery>true</delivery>
<pref>Платье</pref>
<vendor>GLEM</vendor>
<vendorCode>55709</vendorCode>
<model>0301 Платье-рубашка</model>
<description><![CDATA[<p style="text-align: justify;"><strong>Состав:&nbsp;</strong>рубашечный хлопок&nbsp;(80% хлопок, 20% полиэстер)&nbsp;&nbsp;</p>
<p style="text-align: justify;"><strong>Растяжимость:&nbsp;</strong></p>
<p style="text-align: justify;"><strong>Размерная сетка модели:</strong>&nbsp;50, 52, 54,56, 58&nbsp;</p>
<p style="text-align: justify;"><strong>Параметры:&nbsp;</strong>длина изделия: 50р-52р-97 см, 54р-98 см, 56-58р-100 см. Длина рукава: 50р-54р-61 см, 56р-58р-62 см.&nbsp;</p>
<p style="text-align: justify;">Рост модели на фото - 177 см. Обхваты: 96-74-106.&nbsp;</p><p style="text-align: center;"><strong>Замеры изделия (см)</strong>&nbsp;</p>
<table style="margin-left: auto; margin-right: auto;" border="0">
<tbody>
<tr>
<td colspan="2">&nbsp;</td>
<td>50</td>
<td>52</td>
<td>54</td>
<td>56</td>
<td>58</td>
</tr>
<tr>
<td>1.</td>
<td>ОГ изделия&nbsp;</td>
<td>112</td>
<td>116</td>
<td>120</td>
<td>124</td>
<td>128</td>
</tr>
<tr>
<td>2.</td>
<td>ОТ изделия&nbsp;</td>
<td>110</td>
<td>114</td>
<td>120</td>
<td>124</td>
<td>128</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>ОБ изделия&nbsp;</td>
<td>124</td>
<td>128</td>
<td>132</td>
<td>136</td>
<td>140</td>
</tr>
<tr>
<td>3.</td>
<td>Длина изделия по спинке</td>
<td>97</td>
<td>97</td>
<td>98</td>
<td>100</td>
<td>100</td>
</tr>
<tr>
<td>4.</td>
<td>Длина изделия по полочке</td>
<td>100</td>
<td>100</td>
<td>101</td>
<td>103</td>
<td>103</td>
</tr>
<tr>
<td>5.</td>
<td>Длина рукава&nbsp;</td>
<td>61</td>
<td>61</td>
<td>61</td>
<td>62</td>
<td>62</td>
</tr>
<tr>
<td>6.</td>
<td>Обхват руки вверху</td>
<td>38</td>
<td>39</td>
<td>40</td>
<td>42</td>
<td>43</td>
</tr>
<tr>
<td>7.</td>
<td>Обхват руки внизу</td>
<td>23</td>
<td>24</td>
<td>25</td>
<td>26</td>
<td>27</td>
</tr>
<tr>
<td>8.</td>
<td>Ширина по плечам&nbsp;</td>
<td>40</td>
<td>41</td>
<td>42</td>
<td>43</td>
<td>44</td>
</tr>
</tbody>
</table>
<p style="text-align: center;">&nbsp;</p>]]></description>
<manufacturer_warranty>true</manufacturer_warranty><country_of_origin>Украина</country_of_origin><param name="Размер">58, 50, 54</param><param name="Цвет">бордо</param></offer>
"""
offer = json.loads(json.dumps(xmltodict.parse(offer1), indent=4))["offer"]
print(offer)

def func(offer):
    CategoryId = offer["categoryId"]
    title = offer["model"]
    text = offer["description"]
    photo = offer["picture"]
    price = offer["price"]
    size = offer["avail"]["size"]
    variants = {}
    for variant in size:
        variants[variant["#text"]] = variant["@quantity"]
    param = offer["param"]
    color = param[1]["#text"]
    external_id = offer["@id"]
    products = []
    i = 0
    for size, quantity in variants.items():
        i += 1
        try:
            photo_ = photo[i]
        except IndexError:
            photo_ = ''
        variant = {
            "SKU": '',
            "Category": CategoryId,
            "Title": title,
            "Description": '',
            "Text": '',
            "Photo": photo_,
            "Price": price,
            "Quantity": quantity,
            "Price Old": '',
            "Editions": f"Цвет:{color};Размер:{size}",
            "Modifications": '',
            "External ID": external_id + str(i),
            "Parent UID": external_id,
        }
        products.append(variant)
    parent = {
        "SKU": '',
        "Category": CategoryId,
        "Title": title,
        "Description": '',
        "Text": text,
        "Photo": photo[0],
        "Price": '',
        "Quantity": '',
        "Price Old": '',
        "Editions": '',
        "Modifications": '',
        "External ID": external_id,
        "Parent UID": '',
    }
    return parent, products
print(func(offer))