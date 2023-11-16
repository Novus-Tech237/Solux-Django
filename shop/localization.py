import geocoder

def get_country_from_ip(ip_address):
    g = geocoder.ip(ip_address)
    if g and g.country:
        print(g.country)  # Add this line to check the country value
        return g.country
    else:
        return None