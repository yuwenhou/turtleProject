import turtle

# 把乌龟的图形换成三角形
turtle.begin_poly()

turtle.fd(10)
turtle.left(144)
turtle.fd(10)
turtle.left(144)
turtle.fd(10)
turtle.left(144)
turtle.fd(10)
turtle.left(144)
turtle.fd(10)
turtle.left(144)

turtle.end_poly()
p = turtle.get_poly()
turtle.register_shape("pic",p)
pic_pen = turtle.Turtle()
pic_pen.shape("pic")
pic_pen.fd(200)
pic_pen.left(90)
pic_pen.fd(200)
pic_pen.left(90)
pic_pen.fd(200)
pic_pen.left(90)
pic_pen.fd(200)
pic_pen.left(90)
