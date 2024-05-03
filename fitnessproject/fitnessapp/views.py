from django.shortcuts import render, redirect, get_object_or_404
import random, os, requests, json, time
from datetime import datetime, timedelta

from .models import UserAccountDetails, DailyTracking, PaymentsTracking

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from django.conf import settings
from django.core.files.storage import FileSystemStorage

# media_full_path = settings.MEDIA_ROOT + "\playapp_data"
upload_file_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\fitnessapp\\uploaded_files"
# results_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\fitnessapp\\ResultsFiles"
# file_path = f"{upload_file_full_path}\\{logedIn_user}_{title}_code_file.txt"




def index(request):
    # return HttpResponse('Securix V2    |      index Page')
    return render(request,'fitnessapp/welcome.html')

# def showresult(request):
#     # return HttpResponse('Securix V2    |      index Page')
#     return render(request,'fitnessapp/showresult.html')



def bmical(request):
    return render(request,'fitnessapp/BMI.html')

def bfpcal(request):
    return render(request,'fitnessapp/BFP.html')

def bmrcal(request):
    return render(request,'fitnessapp/BMR.html')

def gymnearme(request):
    return render(request,'fitnessapp/GYMNearMe.html')

def recproducts(request):
    recData = [
    {
        "product_name": "Fashnex Resistance Bands Set for Exercise, Stretching and Workout Toning Tube Kit with Foam Handles, Door Anchor, Ankle Strap and Carrying Bag for Men, Women",
        "image": "fitnessapp/setup/images/recProd/p1img.jpg",
        "product_price": "Rs. 659/-",
        "product_link": "https://amzn.in/d/cxUyyj8",
        "product_description": "Deal of the day for Prime Members: Fashnex Resistance Bands Set for Exercise, Stretching and Workout Toning Tube Kit with Foam Handles, Door Anchor, Ankle Strap and Carrying Bag for Men, Women"
    },
    {
        "product_name": "HealthSense Weight Machine for Kitchen, Kitchen Food Weighing Scale for Health, Fitness, Home Baking & Cooking with Bright LCD, Touch Button, Tare Function & 1 Year Warranty – Chef-Mate KS 63",
        "image": "fitnessapp/setup/images/recProd/p2img.jpg",
        "product_price": "Rs. 699/-",
        "product_link": "https://amzn.in/d/9Hl950C",
        "product_description": "Deal of the day for Prime Members: HealthSense Weight Machine for Kitchen, Kitchen Food Weighing Scale for Health, Fitness, Home Baking & Cooking with Bright LCD, Touch Button, Tare Function & 1 Year Warranty – Chef-Mate KS 63"
    },
    {
        "product_name": "beatXP Kitchen Scale Multipurpose Portable Electronic Digital Weighing Scale | Weight Machine With Back light LCD Display | White |10 kg | 2 Year Warranty",
        "image": "fitnessapp/setup/images/recProd/p3img.jpg",
        "product_price": "Rs. 329/-",
        "product_link": "https://amzn.in/d/15sKHLB",
        "product_description": "Deal of the day for Prime Members: beatXP Kitchen Scale Multipurpose Portable Electronic Digital Weighing Scale | Weight Machine With Back light LCD Display | White |10 kg | 2 Year Warranty"
    },
    {
        "product_name": "MuscleBlaze Biozyme Performance Whey Protein | Clinically Tested 50% Higher Protein Absorption | Informed Choice UK, Labdoor USA Certified & US Patent Filed EAF® (Chocolate Hazelnut, 1 kg / 2.2 lb)",
        "image": "fitnessapp/setup/images/recProd/p4img.jpg",
        "product_price": "Rs. 2299/-",
        "product_link": "https://amzn.in/d/67OaUa6",
        "product_description": "Deal of the day: MuscleBlaze Biozyme Performance Whey Protein | Clinically Tested 50% Higher Protein Absorption | Informed Choice UK, Labdoor USA Certified & US Patent Filed EAF® (Chocolate Hazelnut, 1 kg / 2.2 lb)"
    },
    {
        "product_name": "Optimum Nutrition (ON) Gold Standard 100% Whey (2 lbs/907 g) (Double Rich Chocolate) Protein Powder for Muscle Support & Recovery, Vegetarian - Primary Source Whey Isolate",
        "image": "fitnessapp/setup/images/recProd/p5img.jpg",
        "product_price": "Rs. 2899/-",
        "product_link": "https://amzn.in/d/cGZJHbl",
        "product_description": "Deal of the day for Prime Members: Optimum Nutrition (ON) Gold Standard 100% Whey (2 lbs/907 g) (Double Rich Chocolate) Protein Powder for Muscle Support & Recovery, Vegetarian - Primary Source Whey Isolate"
    },
    {
        "product_name": "AS-IT-IS Nutrition ATOM Whey Protein 1kg | 27g protein | Isolate & Concentrate | Double Rich Chocolate | USA Labdoor Certified | With Digestive Enzymes for better absorption",
        "image": "fitnessapp/setup/images/recProd/p6img.jpg",
        "product_price": "Rs. 1766/-",
        "product_link": "https://amzn.in/d/iZgs0A0",
        "product_description": "Deal of the day: AS-IT-IS Nutrition ATOM Whey Protein 1kg | 27g protein | Isolate & Concentrate | Double Rich Chocolate | USA Labdoor Certified | With Digestive Enzymes for better absorption"
    },
    {
        "product_name": "Wellcore - Pure Micronised Creatine Monohydrate Powder (100G, 33 Servings) Lab Tested | Unflavoured | Rapid Absorption | Enhanced Muscle Strength & Power | Fast Recovery | Increased Muscle Mass",
        "image": "fitnessapp/setup/images/recProd/p7img.jpg",
        "product_price": "Rs. 599/-",
        "product_link": "https://amzn.in/d/5zskrGT",
        "product_description": "Limited-time deal: Wellcore - Pure Micronised Creatine Monohydrate Powder (100G, 33 Servings) Lab Tested | Unflavoured | Rapid Absorption | Enhanced Muscle Strength & Power | Fast Recovery | Increased Muscle Mass"
    }
]

    content = {'recData' : recData,}

    return render(request,'fitnessapp/recproducts.html', content)

def payWall(request):

    if request.method == 'POST':
        # Retrieve the form data
        card_number = request.POST.get('cardnumber')
        cardholder_name = request.POST.get('cardholdername')
        expiration_month = request.POST.get('datemonth')
        expiration_year = request.POST.get('dateyear')
        cvv = request.POST.get('cvvdata')
        
        # Print the data (replace print with logging if you want to log it)
        print("Card Number:", card_number)
        print("Cardholder Name:", cardholder_name)
        print("Expiration Month:", expiration_month)
        print("Expiration Year:", expiration_year)
        print("CVV:", cvv)

        '''
        user_name = models.CharField(max_length=50)
    
        plan = models.CharField(max_length=100)
        amount = models.CharField(max_length=100)
        status = models.CharField(max_length=100) # success / fail
        
        timestamp = models.CharField(max_length=100)
        '''
        checkstatus = 'success'
        logged_in_user = request.user.username

        current_time = datetime.now()

        # Format the current date and time
        formatted_time = current_time.strftime("%d/%m/%y %H:%M:%S")


        paydetails = PaymentsTracking.objects.create(
                    user_name=logged_in_user,
                    plan='prime',
                    amount='1000',
                    status= checkstatus,
                    timestamp= formatted_time,
                )

        user_account = UserAccountDetails.objects.get(user_name=logged_in_user)
        user_account.accountPack = 'prime'
        user_account.save()
        
        # Here you can perform further processing like payment processing, etc.
        
        # Return an HTTP response
        # return HttpResponse("Payment successful. Thank you!")
        return redirect('dashboard')


    
    content = {'amount' : 1000,}
    return render(request,'fitnessapp/payWall.html', content)


# http://127.0.0.1:8000/update_account_plan/?plan=prime
def update_account_plan(request):
    # Get the logged-in user's username
    logged_in_user = request.user.username
    
    # Check if the request has the 'plan' parameter
    plan_param = request.GET.get('plan', None)
    if plan_param == 'prime' or plan_param == 'free' :
        # Update the database for the logged-in user where user_name = logged_in_user
        try:
            user_account = UserAccountDetails.objects.get(user_name=logged_in_user)
            user_account.accountPack = plan_param
            user_account.save()
            # return HttpResponse("Account plan updated to 'prime' successfully.")
            return redirect('dashboard')
        
        except UserAccountDetails.DoesNotExist:
            # return HttpResponse("User account not found.")
            return redirect('buyprime')
    else:
        # return HttpResponse("Invalid plan parameter.")
        return redirect('buyprime') 


def buyprime(request):
    logedIn_user = request.user.username
    
    # Query the database to get all records for the logged-in user
    AccounDetails = UserAccountDetails.objects.filter(user_name=logedIn_user)


    freeplandetails = {
        'title': "Free",
        'time': "Forever",
        'amount': "FREE",
        'service': ["GYM near Me", "Yoga", "BMI", "BFP", "BMR", "Exercises"],
        }

    primeplandetails = {
        'title': "Prime",
        'time': "365 Days",
        'amount': "1000",
        'service': ["Daily Tracking", "Recommend Diet", "GYM near Me", "Yoga", "BMI", "BFP", "BMR", "Exercises"],
        }

    context = {
        'freeplan': freeplandetails,
        'primeplan': primeplandetails,
        'AccounDetails': AccounDetails,
        }
    return render(request,'fitnessapp/BuyPrime.html', context)

def yoga(request):
    yogadetails = [
        {
            "name": "Mountain Pose (Tadasana)",
            "description": "Stand tall with feet together, arms at your sides, and shoulders relaxed. Engage your core, lift your chest, and reach your arms overhead with palms facing each other. Hold the pose for several breaths.",
            "benefits": [
                "Improves posture",
                "Strengthens thighs, knees, and ankles",
                "Reduces flat feet",
                "Relieves sciatica",
                "Improves digestion"
            ]
        },
        {
            "name": "Tree Pose (Vrksasana)",
            "description": "Stand tall and shift your weight onto your left foot. Bend your right knee and place the sole of your right foot on your inner left thigh or calf. Bring your palms together in front of your chest or extend your arms overhead. Hold for balance, then switch sides.",
            "benefits": [
                "Improves balance",
                "Strengthens thighs, calves, ankles, and spine",
                "Stretches groin and inner thighs",
                "Improves focus and concentration"
            ]
        },
        {
            "name": "Downward-Facing Dog (Adho Mukha Svanasana)",
            "description": "Start on your hands and knees with your wrists under your shoulders and knees under your hips. Exhale and lift your knees away from the floor, keeping them slightly bent. Press your palms into the mat and lengthen your spine, forming an inverted V shape with your body. Hold for several breaths.",
            "benefits": [
                "Stretches shoulders, hamstrings, calves, and hands",
                "Strengthens arms, legs, and core",
                "Improves circulation",
                "Relieves back pain"
            ]
        },
        {
            "name": "Warrior II (Virabhadrasana II)",
            "description": "Stand with your feet wide apart, facing sideways. Turn your right foot out 90 degrees and your left foot slightly inwards. Bend your right knee directly over your ankle and extend your arms parallel to the floor, reaching out in opposite directions. Gaze over your right fingertips. Hold for several breaths, then switch sides.",
            "benefits": [
                "Strengthens legs, arms, and core",
                "Stretches hips, groin, and shoulders",
                "Improves stamina and concentration",
                "Energizes the entire body"
            ]
        },
        {
            "name": "Child's Pose (Balasana)",
            "description": "Kneel on the mat with your big toes touching and knees apart. Sit back on your heels and fold forward, draping your torso over your thighs. Extend your arms in front of you or rest them alongside your body with palms facing up. Relax your forehead on the mat and breathe deeply.",
            "benefits": [
                "Stretches hips, thighs, and ankles",
                "Relieves back and neck pain",
                "Calms the mind and relieves stress",
                "Restores balance and equilibrium"
            ]
        },
        {
            "name": "Cobra Pose (Bhujangasana)",
            "description": "Lie on your stomach with your palms flat on the ground under your shoulders. Press the tops of your feet and thighs into the floor. Inhale and lift your chest off the ground, straightening your arms while keeping your elbows close to your body. Look up or slightly forward, and hold the pose for several breaths.",
            "benefits": [
                "Strengthens the spine, shoulders, and arms",
                "Stretches the chest, abdomen, and shoulders",
                "Improves posture",
                "Helps relieve stress and fatigue"
            ]
        },
        {
            "name": "Seated Forward Bend (Paschimottanasana)",
            "description": "Sit on the floor with your legs extended in front of you and feet flexed. Inhale to lengthen your spine, then exhale to hinge at your hips and fold forward, reaching for your feet or shins. Keep your spine straight and avoid rounding your back. Hold the stretch for several breaths.",
            "benefits": [
                "Stretches the spine, hamstrings, and lower back",
                "Calms the mind and relieves stress",
                "Improves digestion and stimulates the internal organs",
                "Helps reduce anxiety and fatigue"
            ]
        },
        {
            "name": "Bridge Pose (Setu Bandhasana)",
            "description": "Lie on your back with your knees bent and feet hip-width apart, flat on the floor. Press your feet and arms into the ground as you lift your hips towards the ceiling. Interlace your fingers under your back and roll your shoulders under, lifting your chest towards your chin. Hold the pose for several breaths.",
            "benefits": [
                "Strengthens the back, glutes, and legs",
                "Stretches the chest, neck, and spine",
                "Improves flexibility in the spine and hip flexors",
                "Calms the brain and reduces anxiety"
            ]
        },
        {
            "name": "Corpse Pose (Savasana)",
            "description": "Lie on your back with your legs extended and arms by your sides, palms facing up. Close your eyes and relax your entire body, letting go of any tension or effort. Focus on your breath and allow your mind to become still. Remain in this pose for several minutes, allowing your body to rest and rejuvenate.",
            "benefits": [
                "Promotes deep relaxation and stress relief",
                "Reduces anxiety and tension",
                "Helps improve sleep quality",
                "Allows the body and mind to integrate the benefits of the practice"
            ]
        },
        {
            "name": "Chair Pose (Utkatasana)",
            "description": "Stand tall with your feet together and arms by your sides. Inhale and raise your arms overhead, palms facing each other. Exhale and bend your knees, lowering your hips as if sitting back in a chair. Keep your chest lifted and gaze forward. Hold the pose for several breaths.",
            "benefits": [
                "Strengthens the thighs, calves, and ankles",
                "Tones the core and back muscles",
                "Stretches the shoulders and chest",
                "Improves balance and concentration"
            ]
        },
        {
            "name": "Extended Triangle Pose (Utthita Trikonasana)",
            "description": "Stand with your feet wide apart, right foot turned out 90 degrees and left foot turned in slightly. Extend your arms to the sides at shoulder height. Shift your hips to the left as you reach your right hand towards your right ankle, shin, or a block. Extend your left arm towards the ceiling, keeping your chest open. Gaze up at your left hand. Hold the pose for several breaths, then switch sides.",
            "benefits": [
                "Stretches the hamstrings, groins, hips, and spine",
                "Strengthens the thighs, knees, and ankles",
                "Opens the chest and shoulders",
                "Improves balance and stability"
            ]
        },
        {
            "name": "Plank Pose (Phalakasana)",
            "description": "Begin in a push-up position with your palms flat on the floor, shoulders directly over your wrists, and legs extended behind you. Engage your core and keep your body in a straight line from head to heels. Hold the pose for several breaths, keeping your neck in line with your spine and your gaze slightly forward.",
            "benefits": [
                "Strengthens the core, shoulders, arms, and legs",
                "Improves posture and stability",
                "Increases overall body strength",
                "Prepares the body for more advanced arm balances and inversions"
            ]
        },
        {
            "name": "Cat-Cow Pose (Marjaryasana-Bitilasana)",
            "description": "Start on your hands and knees with your wrists under your shoulders and knees under your hips. Inhale and arch your back, lifting your chest and tailbone towards the ceiling while dropping your belly towards the floor (Cow Pose). Exhale and round your back, tucking your chin towards your chest and drawing your belly button towards your spine (Cat Pose). Flow between the two poses for several breaths.",
            "benefits": [
                "Stretches the spine and neck",
                "Increases flexibility in the back, shoulders, and abdomen",
                "Improves spinal alignment and mobility",
                "Helps relieve tension and stress"
            ]
        },
        {
            "name": "Half Lord of the Fishes Pose (Ardha Matsyendrasana)",
            "description": "Sit on the floor with your legs extended in front of you. Bend your right knee and place your right foot outside your left thigh. Bring your left foot to the outside of your right hip. Inhale and lengthen your spine, then exhale and twist to the right, bringing your left elbow to the outside of your right knee. Hold the pose for several breaths, then switch sides.",
            "benefits": [
                "Stretches the spine, shoulders, and hips",
                "Improves digestion and detoxification",
                "Increases flexibility in the spine and chest",
                "Relieves mild back pain and sciatica"
            ]
        },
        {
            "name": "Legs-Up-the-Wall Pose (Viparita Karani)",
            "description": "Sit with your right side against a wall and your knees bent. Swing your legs up the wall as you lower your upper body to the floor, keeping your shoulders and head on the ground. Extend your legs up the wall and rest your arms by your sides or place your hands on your belly. Close your eyes and relax in the pose for several minutes.",
            "benefits": [
                "Promotes relaxation and reduces stress",
                "Improves circulation and relieves swollen ankles",
                "Stretches the back of the legs and spine",
                "Calms the nervous system and soothes the mind"
            ]
        }
    ]

    context = {
        'yogadetails': yogadetails,
        }

    return render(request,'fitnessapp/Yoga.html', context)


def exercises(request):
    armsData = [
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Incline Bicep Curl.jpeg",
            "title": "Incline Bicep Curl",
            "description": "Incline dumbbell curls target your biceps brachii, which is the biggest muscle in the biceps region.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Concentration Curl.jpeg",
            "title": "Concentration Curl",
            "description": "Concentration curls tone your biceps. Concentration curls build the muscle groups in your arms. Concentration curls help you practice your lifting form.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Twisting Dumbbell Curl.jpeg",
            "title": "Twisting Dumbbell Curl",
            "description": "As with all biceps curls, the twisting standing dumbbell version is designed to build upper arm strength.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Underhand Seated Row.png",
            "title": "Underhand Seated Row",
            "description": "Seated underhand-grip cable row is a exercise machine exercise that primarily targets the middle back and to a lesser degree also targets the biceps, lats, lower back and shoulders.",
            "link": "yt.com"
        }
        ]
    coreData = [
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Hollowman.jpeg",
            "title": "Hollowman",
            "description": "The hollow hold helps strengthen the muscles that stabilize your lower back during athletic and everyday movements.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/High Plank.webp",
            "title": "High Plank",
            "description": "A high plank is a bodyweight exercise that activates muscle groups throughout your body—including your core muscles, glutes, quads, hamstrings, and calves.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Glute Bridge.gif",
            "title": "Glute Bridge",
            "description": "It works the hamstrings, lower back, abs, in addition to the glutes.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Superman pull.jpeg",
            "title": "Superman pull",
            "description": "This move targets your lower back (erector spinae muscles), abs, glutes, hamstrings, and upper back.",
            "link": "yt.com"
        }
        ]
    legsData = [
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Squats.avif",
            "title": "Squats",
            "description": "As you exercise, the movement strengthens your tendons, bones, and ligaments around the leg muscles.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Lunges.avif",
            "title": "Lunges",
            "description": "Lunges are a popular strength training exercise among people wanting to strengthen, sculpt, and tone their bodies, while also improving overall fitness and enhancing athletic performance.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Plank leg lifts.jpg",
            "title": "Plank leg lifts",
            "description": "Adding leg raises can help activate your ab muscles more than regular planks, and they're effective at strengthening your core.",
            "link": "yt.com"
        },
        {
            "image": "fitnessapp/setup/images/exerciseimgs/Single-leg deadlifts.jpeg",
            "title": "Single-leg deadlifts",
            "description": "Single-leg deadlifts work all the major muscles it's two-legged namesake does: the hamstrings, gluteus maximus, gluteus medius, ankles, and the core.",
            "link": "yt.com"
        }
        ]

    context = {
        'armsData': armsData,
        'coreData': coreData,
        'legsData': legsData,
        }
    
    return render(request,'fitnessapp/Exercises.html', context)

def recdiet(request):
    losingweightdiet = [
        {
            "meal": "Breakfast",
            "foods": [
                "Vegetable upma (semolina dish)",
                "Poha (flattened rice) with vegetables",
                "Moong dal chilla (pancake) with mint chutney"
            ]
        },
        {
            "meal": "Lunch",
            "foods": [
                "Dal (lentil curry) with brown rice",
                "Chickpea salad with cucumber and tomato",
                "Mixed vegetable curry with roti (whole wheat flatbread)"
            ]
        },
        {
            "meal": "Dinner",
            "foods": [
                "Grilled fish with sautéed spinach",
                "Tofu stir-fry with bell peppers and broccoli",
                "Paneer (cottage cheese) tikka with green salad"
            ]
        },
        {
            "meal": "Snacks",
            "foods": [
                "Sprouts chaat (mixed sprouts snack)",
                "Roasted chickpeas",
                "Fruit salad with chaat masala (spice mix)"
            ]
        }
    ]

    gainingweighdiet = [
        {
            "meal": "Breakfast",
            "foods": [
                "Masala dosa (fermented crepe) with potato filling",
                "Paratha (stuffed flatbread) with curd and pickle",
                "Vegetable uttapam (thick pancake) with coconut chutney"
            ]
        },
        {
            "meal": "Lunch",
            "foods": [
                "Rajma (kidney bean curry) with rice",
                "Palak paneer (spinach and cottage cheese) with naan (leavened bread)",
                "Vegetable biryani (spiced rice dish) with raita (yogurt dip)"
            ]
        },
        {
            "meal": "Dinner",
            "foods": [
                "Chicken curry with roti or rice",
                "Aloo paratha (potato-stuffed flatbread) with butter",
                "Mutton biryani with cucumber raita"
            ]
        },
        {
            "meal": "Snacks",
            "foods": [
                "Samosa (pastry filled with spiced potatoes)",
                "Paneer tikka (grilled cottage cheese) with mint chutney",
                "Mango lassi (yogurt-based drink) with almonds"
            ]
        }
    ]

    context = {
        'losingweightdiet': losingweightdiet,
        'gainingweighdiet': gainingweighdiet,
        }

    return render(request,'fitnessapp/RecommendDiet.html', context)

def profieview(request):
    logedIn_user = request.user.username
    
    # Query the database to get all records for the logged-in user
    AccounDetails = UserAccountDetails.objects.filter(user_name=logedIn_user)
    PayDetails = PaymentsTracking.objects.filter(user_name=logedIn_user)

    data = DailyTracking.objects.filter(user_name=logedIn_user)

    if data:
        # Sort the queryset based on the primary key in descending order
        sorted_data = data.order_by('-id')
        # Retrieve the last entry
        last_entry = sorted_data.first()
        # Check if the last_entry has imgPath field
        if hasattr(last_entry, 'imgPath'):
            # Retrieve the value of imgPath
            img_path = last_entry.imgPath
            # Print the imgPath
            print("Image Path:", img_path)
        else:
            img_path = "fitnessapp\setup\images\profilepic.jpeg"
            print("imgPath field not found in the last entry")
    else:
        img_path = "fitnessapp\setup\images\profilepic.jpeg"
        print("No data available")

    enddatelist = []
    for payment in PayDetails:
        print("timestamp: ", payment.timestamp)
        timestamp_str = payment.timestamp

        timestamp = datetime.strptime(timestamp_str, "%d/%m/%y %H:%M:%S")

        # Calculate the date 365 days from the given timestamp
        new_timestamp = timestamp + timedelta(days=365)

        # Format the new timestamp
        new_timestamp_str = new_timestamp.strftime("%d/%m/%y %H:%M:%S")
        enddatelist.append(new_timestamp_str)
    
    print("enddatelist: ", enddatelist)

    context = {
        'AccounDetails': AccounDetails,
        'logedIn_user' : logedIn_user,
        'PayDetails'   : PayDetails,
        'enddate'      : enddatelist,
        'img_path'      : img_path,
        }
    
    return render(request, 'fitnessapp/profieview.html', context)



# -------------------------------------------------------------------------------------------------

def dashboard(request):

    logedIn_user = request.user.username
    
    # Query the database to get all records for the logged-in user
    AccounDetails = UserAccountDetails.objects.filter(user_name=logedIn_user)

    context = {
        'AccounDetails': AccounDetails,
        'logedIn_user': logedIn_user,
        }
    
    return render(request, 'fitnessapp/dashboard.html', context)

def seetransformation(request):

    logedIn_user = request.user.username
    
    # Query the database to get all records for the logged-in user
    trackDetails = DailyTracking.objects.filter(user_name=logedIn_user)

    context = {
        'trackDetails': trackDetails,
        'logedIn_user': logedIn_user,
        }
    
    return render(request, 'fitnessapp/seetransformation.html', context)

def dailytracking(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        height = request.POST['height']
        weight = request.POST['weight']
        calorie = request.POST['calorie']

        logedIn_user = request.user.username

        current_time = datetime.now()
        formatted_time = current_time.strftime("%d/%m/%y %H:%M:%S")
        timestamp = formatted_time



        if uploaded_file.name.endswith(('.png', '.jpeg', '.jpg')):
            # fs = FileSystemStorage(location=settings.STATIC_MEDIA_ROOT + '/static/fitnessapp/uploaded_files')
            # fs.save(uploaded_file.name, uploaded_file)

            formatted_time = formatted_time.replace('/', '_')  # Replace colons with underscores
            formatted_time = formatted_time.replace(':', '_')  # Replace colons with underscores
            formatted_time = formatted_time.replace(' ', '_')  # Replace colons with underscores
            
            filename = formatted_time + uploaded_file.name[-4:]  # Appending the extension
            fs = FileSystemStorage(location=settings.STATIC_MEDIA_ROOT + '/static/fitnessapp/uploaded_files')
            filepath = fs.save(filename, uploaded_file)
            imgPath = f"fitnessapp/uploaded_files/{filepath}"
            print("imgPath: ", imgPath)

            # fitnessapp\setup\images\profileTracking.jpg
            # fitnessapp\static\fitnessapp\uploaded_files\
            # 01_05_24_21_05_38.png
            # 01_05_24_21_05_38.png

            dailyDetails = DailyTracking.objects.create(
                    user_name=logedIn_user,
                    imgPath=imgPath,
                    myheight=height,
                    myweigth=weight,
                    toDayCalories=calorie,
                    timestamp=timestamp,
                )
            
            trackDetails = DailyTracking.objects.filter(user_name=logedIn_user)
            length = trackDetails.count()

            user_account = UserAccountDetails.objects.get(user_name=logedIn_user)
            user_account.points = length
            user_account.save()
            # return HttpResponse('File uploaded successfully!')
            return redirect('dashboard')

        else:
            # return HttpResponse('Only .png, .jpeg, .jpg files are allowed!')
            return redirect('dailytracking')

    return render(request, 'fitnessapp/DailyTracking.html')


'''
    imgPath = models.CharField(max_length=300)
    myheight = models.CharField(max_length=100)
    myweigth = models.CharField(max_length=100)
    
    toDayCalories = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)'''








'''
    if request.method == 'POST':

        repo_link = request.POST.get('repo_link')
        title = request.POST.get('title')
        mode = request.POST.get('mode')


    if request.method == 'GET':
        # Extract data from GET request
        myid = request.GET.get('myid')
        user_name = request.GET.get('user_name')
        file_name = request.GET.get('file_name')
        projectName = request.GET.get('projectName')




        # Create LlmFindingResponse object and save it
        llm_finding_response = LlmFindingResponse.objects.create(
            user_name=user_name,
            file_name=file_name,
            projectName=projectName,
            llmresponse=llm_response,
            scanid=myid,

            line=line,
            code=code,
            message=message,
            MetadataCategory=metadata_category,
            MetadataConfidence=metadata_confidence,
            MetadataImpact=metadata_impact,
            CWE=cwe,
            OWASP=owasp,
            Subcategory=subcategory,
            Technology=technology,
            Severity=severity
        )
'''







# Register | Login | Logout Functions

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        phoneno = request.POST['phoneno']
        accountPack = request.POST['accountPack']
        age = request.POST['age']

                
        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            userDetails = UserAccountDetails.objects.create(
                    user_name=username,
                    emailid=email,
                    phoneno=phoneno,
                    accountPack=accountPack,
                    age=age,
                )
            print("userDetails: ", userDetails)
            
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'fitnessapp/register.html', {'error_message': error_message})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'fitnessapp/login.html', {'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view