from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    start = datetime.date(2019,9,29)
    mid_term = datetime.date(2019,10,26)
    first_seminar = datetime.date(2020,1,11)
    growth = datetime.date(2021,9,1)
    today = datetime.date.today()
    total_projects = 14
    done_projects = 2

    mid_term_rate = int(((today-start)/(mid_term-start))*100)
    first_seminar_term_rate = int(((today-start)/(first_seminar-start))*100)
    growth_term_rate = int(((today-start)/(growth-start))*100)
    project_rate = int((done_projects/total_projects)*100)

    pct = {
        'mid_term_rate':mid_term_rate,
        'first_seminar_term_rate':first_seminar_term_rate,
        'growth_term_rate':growth_term_rate,
        'project_rate':project_rate
    }

    return render(request, 'test3/index.html', pct)


def test_index(request):
    test = {'t1':'왜안되지'}

    return render(request, 'test3/test.html', {'t1':'왜안되지'})

