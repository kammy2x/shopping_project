def setup():
    size (600, 600)
    background (255)
#User Account
    fill(0)
    text("Log in/Create Account", 7, 10)
#Logo
    img = loadImage("H&M.png")
    image (img, 190, 0)
    #Menu
    fill(0)
    text("Men", 120, 190)
    fill(0)
    text("Women", 220, 190)
    fill(0)
    text("Boys", 320, 190)
    fill(0)
    text("Girls", 420, 190)
#Sale Image/Caption
    fill(0)
    text("Use code 'SALE' at check-out", 210, 450)
    
    
#About Us
    noFill()
    stroke(0)
    rect(145, 550, 290, 150)
    text("About Us", 260, 570)
    
    
    #right side items 
    fill(0)
    text("Denim Skirt", 490, 230)
    text("Just For Fun Set", 475, 430)
    img = loadImage("denim skirt.jpg")
    image (img, 450, 240, width/4.5, height/4.5)
    img = loadImage ("Just For Fun.jpg")
    image (img, 450, 440, width/4.5, height/4.5)


    Products = {
    "Just For Fun" : "25.00"
    }
    Products["Denim Skirt"] = "15.00"
    
    for x in Products:
        print(Products[x])
    text (Products["Denim Skirt"], 507, 390)
    text (Products["Just For Fun"], 507, 590)


#left side items 
    text("Graphic Tee", 20, 245)
    text("Paradise Tee", 20, 510)
    img = loadImage("men clothes.jpg")
    image(img, 20, 250, width/ 4.5, height/4.5)
    
def draw():
    fill(random(225), random(225), random(225))
    rect (165, 250, 250, 150)
    
    fill(255)
    textSize(70)
    text("S A L E", 175, 350)
