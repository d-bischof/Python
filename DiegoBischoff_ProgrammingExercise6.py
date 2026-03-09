import re 


def main():

    # inputs
    phone: str = input("please enter phone number: ") 
    social: str = input("please enter social security number: ")
    zip_ = input("please enter zip code: ")

    # patterns
    phone_pattern = re.compile(r"\d{10}")   
    social_pattern = re.compile(r"\d{9}")  
    zip_pattern = re.compile(r"\d{5}")     

    # strip formatting
    phone = re.sub(r"[() -]", "", phone)
    social = re.sub(r"[ -]", "", social) 

    # check matches
    isValidPhone = bool(phone_pattern.match(phone))
    isValidSocial = bool(social_pattern.match(social))
    isValidZip = bool(zip_pattern.match(zip_))

    # print first error
    if not isValidPhone:
        print(f"invalid phone number \"{phone}\"")
    elif not isValidSocial:
        print(f"invalid social security number \"{social}\"")
    elif not isValidZip:
        print(f"invalid zip code \"{zip_}\"")



if __name__ == "__main__":
    main()
