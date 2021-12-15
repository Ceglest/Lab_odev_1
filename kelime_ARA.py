paragraf = "A team from the University of Central Florida College of Optics and Photonics, IMEC U.S. and the University of Arizona reported that infrared imaging makes it easier to identify Burmese pythons in the Florida Everglades. For more than 25 years, the invasive snake population has been growing in number in the region, disrupting the delicate ecosystem. And for nearly as long, state officials have been trying to find a way to get rid of them."
 
paragraf= paragraf.replace(".", "")
paragraf = paragraf.replace(",", "")


liste = paragraf.split(" ")
kelime = input("kelime:")

def kelimeAra():
    if kelime in liste:
        print("Kelime bulundu.")
    else:
        print("Kelime bulunamadı.")
    
               
kelimeAra()
            
