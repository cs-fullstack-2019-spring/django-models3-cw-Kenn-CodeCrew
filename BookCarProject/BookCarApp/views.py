from django.http import HttpResponse
from .models import Book, Car


# Create your views here.
def index(request):
    return HttpResponse("TestURL")


def new(request):
    newBook = Book(name="Fault in our Stars", pageNumber=300, genre="Fiction", publishDate="2014-08-07")
    newBook.save()
    return HttpResponse("New entry added!")

def all(request):
    getAllBooks = Book.objects.all()
    allBooksString = ""
    addH1 = ""

    for eachBookInArray in getAllBooks:
        addH1 = "<h1>" + str(eachBookInArray) + "<h1>"
        allBooksString = allBooksString + addH1 + "<br>"

    return HttpResponse(allBooksString)


def greater(request):
    stringOfBooks = ""
    onlyNewBooks = Book.objects.filter(publishDate__gte = '2018-01-01')

    for eachBook in onlyNewBooks:
        stringOfBooks += str(eachBook) + "<br>"

    htmlToReturn = "<h1>Here are the new books</h1>" + stringOfBooks
    return HttpResponse(htmlToReturn)


def update(request):
    updateThisList = Book.objects.filter(publishDate__gte= "2018-01-01")

    for eachBookInArray in updateThisList:
        eachBookInArray.genre = "fiction"
        eachBookInArray.save()

    return HttpResponse(updateThisList)