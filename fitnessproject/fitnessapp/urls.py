from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profieview/", views.profieview, name="profieview"),
    path("buyprime/", views.buyprime, name="buyprime"),
    path("payWall/", views.payWall, name="payWall"),

    path("update_account_plan/", views.update_account_plan, name="update_account_plan"),


    # path("upload_file/", views.upload_file, name="upload_file"),

    path("bmical/", views.bmical, name="bmical"),
    path("bfpcal/", views.bfpcal, name="bfpcal"),
    path("bmrcal/", views.bmrcal, name="bmrcal"),

    path("gymnearme/", views.gymnearme, name="gymnearme"),
    path("exercises/", views.exercises, name="exercises"),
    path("recdiet/", views.recdiet, name="recdiet"),
    path("yoga/", views.yoga, name="yoga"),
    path("dailytracking/", views.dailytracking, name="dailytracking"),
    path("seetransformation/", views.seetransformation, name="seetransformation"),


    # path("repolinkupload/", views.repolinkupload, name="repolinkupload"),
    # path("repoScan/", views.repoScan, name="repoScan"),
    # path("showresult/<int:myid>", views.showresult, name="showresult"),
    # path('llm_finding/', views.save_llm_finding_response, name='save_llm_finding_response'),
    # path("llmsolution/<int:myid>", views.llmsolution, name="llmsolution"),




    path('user_login/',      views.user_login,     name='user_login'),
    path('user_logout/',     views.user_logout,    name='user_logout'),
    path('user_register/',   views.user_register,  name='user_register'),

]