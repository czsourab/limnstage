
from django.urls import path
from. import views, uploader, index, thelimn, profile, update, answering, dyload ,ansupdate, subartist, webdocs, extralimn, limnvarification
from django.contrib.sitemaps.views import sitemap
from limnstageapp.views import limnSitemap

sitemaps={
    'post' : limnSitemap
}

urlpatterns = [
    path('', index.index, name="index"),
    path('load/', dyload.load, name="load"),
    path('privacy-policy', webdocs.privacy, name="privacy"),
    path('varification-limns', limnvarification.limnvarification, name="limnvarification"),
    path('unsolved-queries', extralimn.unsolved, name="unsolved"),
    path('recent-articles', extralimn.recentarticle, name="recentarticle"),
    path('contact-us', webdocs.contact, name="contact"),
    path('subscribe-the-artist', subartist.subtheartist, name="subtheartist"),
    path('ads.txt', views.adstxt, name="adstxt"),
    path('signtoupcz', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('limning', views.limning, name="limning"),
    path('uploader', uploader.uploader, name="uploader"),
    path('ansupdate/<int:id>/<str:title>', ansupdate.ansupdate, name="ansupdate"),
    path('answering/<int:id>/<str:title>', answering.answering, name="answering"),
    path('thelimn/<int:id>/<str:title>', thelimn.thelimn, name="thelimn"),
    path('update/<int:id>/<str:title>', update.update, name="update"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('<str:name>', profile.profile, name="profile"),
    path('<str:name>/solved', profile.solved, name="profile"),
    path('<str:name>/asked-by-people', profile.askedbypeople, name="profile")
]
