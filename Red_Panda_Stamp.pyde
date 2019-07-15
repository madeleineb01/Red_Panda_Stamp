size(512, 512)


fill(201, 85, 22)
ellipse(260, 260, 220, 150) #head

fill(0,0,0)
ellipse(220, 230, 20, 40) #eyes
ellipse(300, 230, 20, 40)

fill(255, 234, 196)
ellipse(260, 280, 70, 40) #mouth

fill(0, 0, 0)
ellipse(260, 270, 15, 10) #nose

translate(200, 75)
fill(201, 85, 22)
arc(150, 100, 80, 80, 0, PI, OPEN)
translate(200, 75)
rotate(PI/3)
