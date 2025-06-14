from django.shortcuts import render, get_object_or_404
from .models import Person, Relation

def tree(request):
    # Получаем всех людей и связи
    persons = Person.objects.all()
    relations = Relation.objects.all()

    # Подготавливаем списки словарей для шаблона
    nodes = []
    for p in persons:
        nodes.append({
            'id': p.id,
            'name': p.name,
            'birth_date': p.birth_date.isoformat() if p.birth_date else '',
            'photo_url': p.photo.url if p.photo else '',
        })

    edges = []
    for r in relations:
        edges.append({
            'parent': r.parent.id,
            'child': r.child.id,
        })

    return render(request, 'family/tree.html', {
        'nodes': nodes,
        'edges': edges,
    })
def person_detail(request, pk):
    # найдём человека по его PK или выдадим 404
    person = get_object_or_404(Person, pk=pk)

    # получим родителей и детей
    parents = [rel.parent for rel in person.parents.all()]
    children = [rel.child for rel in person.children.all()]

    return render(request, 'family/person_detail.html', {
        'person': person,
        'parents': parents,
        'children': children,
    })
