from datetime import datetime


def version_cp(request):
    ctx = {
        "version":	"0.1.89",
        "current_year": datetime.now().year
    }
    return ctx
