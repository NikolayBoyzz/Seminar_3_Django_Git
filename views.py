from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from myapp1 import models


class IndicationPrice(View):
    def get(self, request, user_id, timespan_in_days) -> HttpResponse:
        client = get_object_or_404(models.Client, pk=user_id)
        timespan = timedelta(days=timespan_in_days)
        orders = models.Order.objects.filter(customer=client).filter(
            date_ordered__gte=(date.today() - timespan)
        )

        o = []
        for order in orders:
            products = order.products.all()
            o.append({"order_data": order, "products": products})

        context = {
            "client": client,
            "orders": o,
            "period": timespan_in_days,
        }
        return render(
            request=request, template_name="myapp2/indication_price.html", context=context
        )