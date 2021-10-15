from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime

app=Flask(__name__)
app.secret_key = 'the random string'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'priyoakashi405@gmail.com'
app.config['MAIL_PASSWORD'] = '5255452554'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/agroaid"
db = SQLAlchemy(app)



class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    phone_number = db.Column(db.String(120),  nullable=False)
    message = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(120),  nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(120),  nullable=False)
    tagline = db.Column(db.String(120),  nullable=False)
    content = db.Column(db.String(120),  nullable=False)
    image = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120),  nullable=True)
    active = db.Column(db.String(120), nullable=False)
    post_by = db.Column(db.String(120), nullable=False)

class Products(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(120),  nullable=False)
    image = db.Column(db.String(120),  nullable=False)
    price = db.Column(db.String(120),  nullable=False)
    catagory = db.Column(db.String(120),  nullable=False)
    description = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(120),  nullable=True)
    active = db.Column(db.String(120),  nullable=False)


class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120),  nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    mobile = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    gender = db.Column(db.String(120),  nullable=False)
    division = db.Column(db.String(120),  nullable=False)
    district = db.Column(db.String(120),  nullable=False)
    upozila = db.Column(db.String(120),  nullable=False)
    


class Expert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    image = db.Column(db.String(120),  nullable=False)
    address = db.Column(db.String(120),  nullable=False)
    workspace = db.Column(db.String(120),  nullable=False)
    research = db.Column(db.String(120),  nullable=False)
    education = db.Column(db.String(120),  nullable=False)
    username = db.Column(db.String(120),  nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(120),  nullable=False)


class Experthelp(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    expert_id = db.Column(db.Integer, primary_key=True)
    expert_name = db.Column(db.String(80), nullable=False)
    person = db.Column(db.String(120),  nullable=False)
    problem = db.Column(db.String(120),  nullable=False)
    problem_image = db.Column(db.String(120),  nullable=False)




class Orders(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(80), nullable=False)
    product_name = db.Column(db.String(120),  nullable=False)
    user_name= db.Column(db.String(120),  nullable=False)
    user_division = db.Column(db.String(120),  nullable=False)
    user_district = db.Column(db.String(120),  nullable=False)
    user_upozila = db.Column(db.String(120),  nullable=False)
    full_address = db.Column(db.String(120),  nullable=False)
    payment_method = db.Column(db.String(120),  nullable=False)
    product_price = db.Column(db.String(120),  nullable=False)



"""----------home/post--------"""

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    return render_template("home.html",blog=posts)

@app.route("/about")
def about():
    post = Posts.query.filter_by().all()
    return render_template("about.html")


@app.route("/post")
def index():
    posts = Posts.query.filter_by().all()
    print(posts)
    return render_template("index.html", blog=posts)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html',blog=post)




"""------------------agromart------------"""

@app.route("/agromart")
def agromart():
    product = Products.query.filter_by().all()
    return render_template("agromart.html",product=product)

@app.route("/buy_product")
def buy_product():
    product = Products.query.filter_by().all()
    return render_template("buy_product.html",product=product)

@app.route("/rent_product")
def rent_product():
    product = Products.query.filter_by().all()
    return render_template("rent_product.html",product=product)



@app.route("/product/<string:post_slug>", methods=['GET'])
def product(post_slug):
    product=Products.query.filter_by(slug=post_slug).first()
    return render_template("product.html",product=product)

@app.route("/order/<string:product_id>", methods=["GET","POST"])
def order(product_id):
    if "user" in session:
        order=Products.query.filter_by(sno=product_id).first()
        order.sno=product_id
        data=User.query.filter_by(email=session["user"]).first()
        if request.method =="POST":
            box_full_address=request.form.get("form_full_address")
            box_payment_method=request.form.get("user_payment_method")
            entry=Orders(full_address=box_full_address,payment_method=box_payment_method,product_name=order.name,product_id=product_id,product_price=order.price,user_name=data.last_name,user_division=data.division,user_district=data.district,user_upozila=data.upozila)
            db.session.add(entry)
            db.session.commit()
            return "your order is taken"
        return render_template("order.html",order=order)
    else:
        return redirect("/user_login")


"""------------dashboard-----------------"""





@app.route("/post_table")
def post_table():
    posts = Posts.query.filter_by().all()
    return render_template("post_table.html",posts=posts)


@app.route("/post_edit/<string:sno>",methods=["GET","POST"])
def post_edit(sno):
    if request.method =="POST":
        box_title=request.form.get("post_title")
        box_slug=request.form.get("post_slug")
        box_tagline=request.form.get("post_tagline")
        box_content=request.form.get("post_content")
        box_image=request.form.get("post_image")
        box_date=request.form.get("post_date")

        if sno =="0":
            entry=Posts(title=box_title,slug=box_slug,tagline=box_tagline,content=box_content,image=box_image,date=datetime.now(),active="1",post_by="Admin")
            db.session.add(entry)
            db.session.commit()
            return redirect("/post_table")
        else:
            posts=Posts.query.filter_by(sno=sno).first()
            posts.title=box_title
            posts.slug=box_slug
            posts.tagline=box_tagline
            posts.content=box_content
            posts.image=box_image
            db.session.commit()
            return redirect("/post_table")
    posts=Posts.query.filter_by(sno=sno).first()
    return render_template("post_edit.html",posts=posts,sno=sno)



@app.route("/user_post_edit/<string:sno>",methods=["GET","POST"])
def user_post_edit(sno):
    if request.method=="POST":
        box_title=request.form.get("post_title")
        box_slug=request.form.get("post_slug")
        box_tagline=request.form.get("post_tagline")
        box_content=request.form.get("post_content")
        box_image=request.form.get("post_image")
        box_date=request.form.get("post_date")


        posts=Posts.query.filter_by(sno=sno).first()
        posts.title=box_title
        posts.slug=box_slug
        posts.tagline=box_tagline
        posts.content=box_content
        posts.image=box_image
        db.session.commit()
        return redirect("/user_timeline")
    posts=Posts.query.filter_by(sno=sno).first()    
    return render_template("user_post_edit.html",posts=posts,sno=sno)
    

@app.route("/delete_post/<string:sno>",methods=["GET","POST"])
def delete_post(sno):
    posts=Posts.query.filter_by(sno=sno).first()
    db.session.delete(posts)
    db.session.commit()
    return redirect("/post_table")


@app.route("/user_post",methods=["GET","POST"])
def user_post():
        if request.method =="POST":
            box_title=request.form.get("post_title")
            box_slug=request.form.get("post_slug")
            box_tagline=request.form.get("post_tagline")
            box_content=request.form.get("post_content")
            box_image=request.form.get("post_image")
            box_date=request.form.get("post_date") 
            dt=session["user"]
            users=User.query.filter_by(email=dt).first()
            entry=Posts(title=box_title,slug=box_slug,tagline=box_tagline,content=box_content,image=box_image,date=datetime.now(),active="0",post_by=users.last_name)
            db.session.add(entry)
            db.session.commit()
            return redirect("/profile")
        return render_template("user_post.html")




@app.route("/product_table")
def product_table():
    products = Products.query.filter_by().all()
    return render_template("product_table.html",products=products)


@app.route("/product_edit/<string:sno>",methods=["GET","POST"])
def product_edit(sno):
    if request.method =="POST":
        box_name=request.form.get("product_name")
        box_slug=request.form.get("product_slug")
        box_image=request.form.get("product_image")
        box_price=request.form.get("product_price")
        box_description=request.form.get("product_description")
        box_catagory=request.form.get("product_catagory")
        box_date=request.form.get("product_date")
        
        if sno =="0":
            entry=Products(name=box_name,slug=box_slug,image=box_image,price=box_price,catagory=box_catagory,description=box_description,date=datetime.now())
            db.session.add(entry)
            db.session.commit()
            return redirect("/product_table")
        else:
            products=Products.query.filter_by(sno=sno).first()
            products.name=box_name
            products.image=box_image
            products.price=box_price
            products.catagory=box_catagory
            products.description=box_description
            db.session.commit()
            return redirect("/product_table")
    products=Products.query.filter_by(sno=sno).first()
    return render_template("product_edit.html",products=products,sno=sno)


@app.route("/delete_product/<string:sno>",methods=["GET","POST"])
def delete_product(sno):
    products=Products.query.filter_by(sno=sno).first()
    db.session.delete(products)
    db.session.commit()
    return redirect("/product_table")


@app.route("/user_product",methods=["GET","POST"])
def user_product():
    if request.method =="POST":
        box_name=request.form.get("product_name")
        box_slug=request.form.get("product_slug")
        box_image=request.form.get("product_image")
        box_price=request.form.get("product_price")
        box_description=request.form.get("product_description")
        box_catagory=request.form.get("product_catagory")
        box_date=request.form.get("product_date")
        entry=Products(name=box_name,slug=box_slug,image=box_image,price=box_price,catagory=box_catagory,description=box_description,date=datetime.now(),active="0")
        db.session.add(entry)
        db.session.commit()
        return redirect("/profile")
    return render_template("user_product.html")

@app.route("/user_table")
def user_table():
    users = User.query.filter_by().all()
    return render_template("user_table.html",users=users)


@app.route("/user_edit/<string:sno>",methods=["GET","POST"])
def user_edit(sno):
    if request.method =="POST":
        box_first_name=request.form.get("first_name")
        box_last_name=request.form.get("last_name")
        box_email=request.form.get("email")
        box_mobile=request.form.get("mobile")
        box_password=request.form.get("password")
        box_division=request.form.get("division")
        box_district=request.form.get("district")
        box_upozila=request.form.get("upozila")
        if sno =="0":
            entry=Products(first_name=box_first_name,last_name=box_last_name,email=box_email,mobile=box_mobile,password=box_password,division=box_division,district=box_district,upozila=box_upozila) 
            db.session.add(entry)
            db.session.commit()
            return redirect("/user_table")
        else:
            users=User.query.filter_by(sno=sno).first()
            users.first_name=box_first_name
            users.last_name=box_last_name
            users.email=box_email
            users.mobile=box_mobile
            users.password=box_password
            users.division=box_division
            users.district=box_district
            users.upozila=box_upozila
            db.session.commit()
            return redirect("/user_table")
    users=User.query.filter_by(sno=sno).first()
    return render_template("user_edit.html",users=users,sno=sno)


@app.route("/delete_user/<string:sno>",methods=["GET","POST"])
def delete_user(sno):
    users=User.query.filter_by(sno=sno).first()
    db.session.delete(users)
    db.session.commit()
    return redirect("/user_table")



@app.route("/expert_table")
def expert_table():
    experts = Expert.query.filter_by().all()
    return render_template("expert_table.html",experts=experts)



@app.route("/expert_edit/<string:id>",methods=["GET","POST"])
def expert_edit(id):
    if request.method =="POST":
        box_name =request.form.get("name")
        box_phone =request.form.get("phone")
        box_image =request.form.get("image")
        box_address =request.form.get("address")
        box_workspace =request.form.get("workspace")
        box_research =request.form.get("research")
        box_education =request.form.get("education")
        box_username =request.form.get("username")
        box_password =request.form.get("password")
        box_email =request.form.get("email")
        if id =="0":
            entry=Expert(name=box_name,phone=box_name,image=box_image,address=box_address,workspace=box_workspace,research=box_research,education=box_education,username=box_username,password=box_password,email=box_email)
            db.session.add(entry)
            db.session.commit()
            return redirect("/expert_table")
        else:
            experts=Expert.query.filter_by(id=id).first()
            experts.name=box_name
            experts.phone=box_phone
            experts.image=box_image
            experts.address=box_address
            experts.workspace=box_workspace
            experts.research=box_research
            experts.education=box_education
            experts.username=box_username
            experts.password=box_password
            experts.email=box_email
            db.session.commit()
            return redirect("/expert_table")
    experts=Expert.query.filter_by(id=id).first()
    return render_template("expert_edit.html",experts=experts,id=id)



@app.route("/delete_expert/<string:id>",methods=["GET","POST"])
def delete_expert(id):
    experts=Experts.query.filter_by(id=id).first()
    db.session.delete(experts)
    db.session.commit()
    return redirect("/expert_table")


@app.route("/expert_help_table")
def expert_help_table():
    experts_help = Experthelp.query.filter_by().all()
    return render_template("expert_help_table.html",experts_help=experts_help)




@app.route("/expert_help_edit/<string:expert_id>",methods=["GET","POST"])
def expert_help_edit(expert_id):
    if request.method =="POST":
        expert_name =request.form.get("expert_name")
        person =request.form.get("person")
        problem =request.form.get("problem")
        problem_image =request.form.get("problem_image")
    
        if expert_id =="0":
            entry=Experthelp(expert_name=expert_name,person=person,problem=problem,problem_image=problem_image)
            db.session.add(entry)
            db.session.commit()
            return redirect("/expert_help_table")
        else:
            experts=Experthelp.query.filter_by(expert_id=expert_id).first()
            experts_help.expert_name=expert_name
            experts_help.person=person
            experts_help.problem=problem
            experts_help.problem_image=problem_image
            db.session.commit()
            return redirect("/expert_help_table")
    experts_help=Experthelp.query.filter_by(expert_id=expert_id).first()
    return render_template("expert_help_edit.html",experts_help=experts_help,expert_id=expert_id)



@app.route("/delete_expert_help/<string:expert_id>",methods=["GET","POST"])
def delete_expert_help(expert_id):
    experts_help=Experthelp.query.filter_by(expert_id=expert_id).first()
    db.session.delete(experts_help)
    db.session.commit()
    return redirect("/expert_help_table")





@app.route("/approval_table")
def approval_table():
    return render_template("approval_table.html")

@app.route("/approve_post")
def approve_post():
    posts=Posts.query.filter_by().all()
    return render_template("approve_post.html",posts=posts)

@app.route("/add_post/<string:sno>", methods=["GET","POST"])
def add_post(sno):
    posts=Posts.query.filter_by(sno=sno).first()
    posts.active="1"
    db.session.commit()
    return redirect("/approve_post")


@app.route("/approve_product")
def approve_product():
    products=Products.query.filter_by().all()
    return render_template("approve_product.html",products=products)

@app.route("/add_product/<string:sno>", methods=["GET","POST"])
def add_product(sno):
    products=Products.query.filter_by(sno=sno).first()
    products.active="1"
    db.session.commit()
    return redirect("/approve_product")

"""---------------expert-------------"""


@app.route("/expert", methods=["GET","POST"])
def expert():
    expert=Expert.query.filter_by().all()
    return render_template("expert.html",expert=expert)



@app.route("/expert_details/<string:box_id>", methods=["GET","POST"])
def expert_details(box_id):
    expert=Expert.query.filter_by(id=box_id).first()
    dt=session["user"]
    posts = User.query.filter_by(email=dt).first()
    if request.method=="POST":
        print("hello")
        box_message=request.form.get("help_message")
        box_image=request.form.get("help_image")
        entry=Experthelp(problem=box_message,problem_image=box_image,expert_id=expert.id,expert_name=expert.name,person=posts.last_name)
        db.session.add(entry)
        db.session.commit()
        return render_template("expert_details.html",expert=expert)
    
    return render_template("expert_details.html",expert=expert)

"""@app.route("/user_login",methods=["GET","POST"])
def user_login():
    if request.method == "POST":
        box_email=request.form["user_email"]
        box_password=request.form["user_password"]
        session["user"]=box_email
        try:
            data = User.query.filter_by(email=box_email,password=box_password).first()
            print(data)
            if data is not None:
                print(session["user"])
                print(data)
                return redirect("/home")
            else:
                return "<script>wrong email or password</script>"
        except:
            return "<h1>database problem </h1>"
    return render_template("user_login.html")"""

@app.route("/expert_login",methods=["GET","POST"])
def expert_login():
    if request.method == "POST":
        box_username=request.form["form_username"]
        box_password=request.form["form_password"]
        try:
            experts = Expert.query.filter_by(username=box_username,password=box_password).first()
            if experts is not None:
                session["expert"]=experts.username
                if "user" in session:
                    session.pop("user")
                return redirect("/")
            else:
                return "<h1>wrong email or password</h1>"
        except:
            return "<h1>database problem </h1>"
    return render_template("expert_login.html")

@app.route("/problem_details/<string:sno>", methods=["GET","POST"])
def problem_details(sno):
    problems=Experthelp.query.filter_by(sno=sno).first()
    return render_template("problem_details.html",problems=problems,sno=sno)


"""-----------------autentication---------------------"""


@app.route("/admin_login",methods=["GET","POST"])
def adminLogin():
    if request.method == "POST":
        name = request.form.get("form_name")
        password = request.form.get("form_password")
        if name == "karim" and password == "12345":
            return render_template("product_table.html")
        else:
            return "wrong Password or email"
    return render_template("admin_login.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        user_first_name = request.form.get("box_first_name")
        user_last_name = request.form.get("box_last_name")
        user_email = request.form.get("box_email")
        user_mobile = request.form.get("box_mobile")
        user_password = request.form.get("box_password")
        user_gender = request.form.get("box_gender")
        user_division = request.form.get("box_division")
        user_district = request.form.get("box_district")
        user_upozila = request.form.get("box_upozila")

        entry=User(first_name=user_first_name,last_name=user_last_name,email=user_email,mobile=user_mobile,password=user_password,gender=user_gender,division=user_division,district=user_district,upozila=user_upozila)
        db.session.add(entry)
        db.session.commit()
        return redirect("/user_login")
    return render_template("signup.html")



@app.route("/user_login",methods=["GET","POST"])
def user_login():
    if request.method == "POST":
        box_email=request.form["user_email"]
        box_password=request.form["user_password"]
        try:
            data = User.query.filter_by(email=box_email,password=box_password).first()  
            if data is not None:
                session["user"]=data.email
                if "expert" in session:
                    session.pop("expert")
                return redirect("/")
            else:
                return "<script>wrong email or password</script>"
        except:
            return "<h1>database problem </h1>"
    return render_template("user_login.html")

"""------------profile------------"""

@app.route("/profile")
def profile():
    if "user" in session:
        dt=session["user"]
        posts = User.query.filter_by(email=dt).first()
        return render_template("profile.html",posts=posts)
    if "expert" in session:
        expert_var=session["expert"]
        posts = Expert.query.filter_by(username=expert_var).first()
        experthelps=Experthelp.query.filter_by(expert_id=posts.id).all()
        return render_template("profile.html",posts=posts,experthelps=experthelps)
        

    else:
        return redirect("/user_login")

@app.route("/user_timeline",methods=["POST","GET"])
def user_timeline():
    dt=session["user"]
    users=User.query.filter_by(email=dt).first()
    blog=Posts.query.filter_by(post_by=users.last_name).all()
    return render_template("user_timeline.html",blog=blog,users=users)



@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/")

@app.route("/logout_expert")
def logout_expert():
    session.pop("expert")
    return redirect("/")




app.run(debug=True)
