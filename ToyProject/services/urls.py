from django.urls import path, include

import services.views

urlpatterns = [
    path("train/",services.views.train_view,name="train"),
    path("predict/",services.views.predict_view,name="predict"),
]
