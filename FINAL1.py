from guizero import Text, TextBox, PushButton, Slider, App, Picture

def SaveFunc():
    Happy=HappySlider.value
    if HappySlider.value == 0:
        HoneyValue = 0
    elif 0 < HappySlider.value <= 19:
        HoneyValue = 1
    elif 20 <= HappySlider.value <= 69:
        HoneyValue = 2
    elif 70 <= HappySlider.value < 100:
        HoneyValue = 3
    elif HappySlider.value >= 100:
        HoneyValue = 5

    Sad = SadSlider.value
    if SadSlider.value == 0:
        AppCidVinValue = 0
        LemonValue=0
    elif 0 < SadSlider.value <= 19:
        AppCidVinValue = 1
        LemonValue =0
    elif 20 <= SadSlider.value <= 69:
        AppCidVinValue = 2
        LemonValue =0
    elif 70 <= SadSlider.value < 100:
        AppCidVinValue = 3
        LemonValue =2
    elif SadSlider.value >= 100:
        AppCidVinValue = 5
        LemonValue =4

    Angry = AngrySlider.value
    if AngrySlider.value == 0:
        MustardValue = 0
        SrirachaValue = 0
    elif 0 < AngrySlider.value <= 19:
        MustardValue = 1
        SrirachaValue=0
    elif 20 <= AngrySlider.value <= 69:
        MustardValue = 2
        SrirachaValue= 0
    elif 70 <= AngrySlider.value < 100:
        MustardValue = 3
        SrirachaValue = 1
    elif AngrySlider.value >= 100:
        MustardValue = 5
        SrirachaValue = 2


    Nervous = NervousSlider.value
    if NervousSlider.value == 0:
        CarrotValue = 0
    elif 0 < NervousSlider.value <= 19:
        CarrotValue = 1
    elif 20 <= NervousSlider.value <= 69:
        CarrotValue = 2
    elif 70 <= NervousSlider.value < 100:
        CarrotValue = 3
    elif NervousSlider.value >= 100:
        CarrotValue = 5

    Feral = FeralSlider.value
    if FeralSlider.value == 0:
        KetchupValue = 0
    elif 0 < FeralSlider.value <= 19:
        KetchupValue = 1
    elif 20 <= FeralSlider.value <= 69:
        KetchupValue = 2
    elif 70 <= FeralSlider.value < 100:
        KetchupValue = 3
    elif FeralSlider.value >= 100:
        KetchupValue = 5


    OrderText= Text(app, size=16, text=(f'''Thank you for using the Coleslaw generator. Please be patient while the machine makes your coleslaw. In case you were wondering, your coleslaw contains
    1 pound of purple cabbage,
    1 pound of green cabbage,
    1/2 cup loosely packed fresh parsley leaves,
    1 cup mayonnaise,
    1 teaspoon celery seeds,
    1/4 teaspoon fine sea salt,
    1/4 teaspoon fresh ground black pepper,
    {HoneyValue} tablespoon(s) of honey,
    {AppCidVinValue} tablespoon(s) of Apple Cider vinegar,
    {LemonValue} tablespoon(s) of Lemon juice,
    {SrirachaValue} tablespoon(s) of Sriracha,
    {CarrotValue} whole grated carrot(s),
    {MustardValue} tablespoon(s) of mustard,
    {KetchupValue} squirt(s) of ketchup, you vile creature.'''))


    LoadingPicture = Picture(app, image="loading-buffering.gif")

    def DestroyLoadingPic():
        LoadingPicture.destroy()
        ColeslawPicture = Picture(app, image="coleslaw.gif", height=347, width=518)

    LoadingPicture.after(5000,DestroyLoadingPic)



app=App(title="Coleslaw Genarator")

WelcomeText= Text(app, text="Welcome to the Coleslaw Genarator! Please input your current emotions to create the perfect coleslaw for the occasion. ",size=14)

HappyText= Text(app, text=""
                          "Happiness Level", size=14)
HappySlider=Slider(app)

SadText= Text(app, text="Sadness Level",size=14)
SadSlider=Slider(app)

AngryText= Text(app, text="Anger Level",size=14)
AngrySlider=Slider(app)

NervousText= Text(app, text="Nervousness Level",size=14)
NervousSlider=Slider(app)

FeralText= Text(app, text="Ferality Level",size=14)
FeralSlider=Slider(app)

ExecuteButton=PushButton(app, command=SaveFunc, text="Make my coleslaw!")

app.display()
