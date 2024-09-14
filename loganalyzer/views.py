from django.http import JsonResponse
from loganalyzer.util_funcs_log import scan_logs

def count_logs(request, date_string):
    print(date_string)
    distinct_count_of_logs = scan_logs(date_string)
    return JsonResponse({'count': distinct_count_of_logs})