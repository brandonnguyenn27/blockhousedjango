from django.shortcuts import render

from django.http import JsonResponse

def candlestick_data(request):
    data = {
        "data": [
            {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
            {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
            {"x": "2023-01-03", "open": 40, "high": 50, "low": 35, "close": 45},
            {"x": "2023-01-04", "open": 35, "high": 45, "low": 30, "close": 40},
            {"x": "2023-01-05", "open": 50, "high": 60, "low": 45, "close": 55},
        ]
    }
    return JsonResponse(data)

def line_chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "data": [10, 20, 30, 40]
    }
    return JsonResponse(data)

def bar_chart_data(request):
    data = {
        "labels": ["Product A", "Product B", "Product C"],
        "data": [100, 150, 200]
    }
    return JsonResponse(data)

def pie_chart_data(request):
    data = {
        "labels": ["Red", "Blue", "Yellow"],
        "data": [300, 50, 100]
    }
    return JsonResponse(data)