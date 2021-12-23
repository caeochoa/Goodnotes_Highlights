import fitz

def find_highlights(page):
    # list to store the co-ordinates of all highlights
    highlights = []
    #colors = []
    # loop till we have highlight annotation in the page
    annot = page.firstAnnot
    while annot:
        if annot.type[0] == 8:
            #colors.append(annot.colors)
            all_coordinates = annot.vertices
            if len(all_coordinates) == 4:
                highlight_coord = fitz.Quad(all_coordinates).rect
                highlights.append([highlight_coord, annot.colors])
            else:
                all_coordinates = [all_coordinates[x:x+4] for x in range(0, len(all_coordinates), 4)]
                for i in range(0,len(all_coordinates)):
                    coord = fitz.Quad(all_coordinates[i]).rect
                    highlights.append([coord, annot.colors])
        annot = annot.next
    return highlights#, colors

def ink2highlight(page):
    annot = page.firstAnnot
    h = []
    while annot:
        if annot.type[0] == 15:
            rect = fitz.Rect(annot.rect.x0, annot.rect.y0+annot.rect.height/3, annot.rect.x1, annot.rect.y1-annot.rect.height/3)
            h.append([rect, annot.colors])
            page.delete_annot(annot)
        annot = annot.next
    for r, c in h:
        x = page.add_highlight_annot(r)
        x.set_colors(colors=c)
        x.update()
    return page

def remove_overlaps(h):
    hl = []
    k = 0
    for i in h:
        #print("Checking intersections with rectangle:", i)
        for j in h:
            #print("Possible rectangle:", j)
            if i.intersects(j) and i != j:
                i.include_rect(j)
                h.pop(h.index(j))
                #print(j, i)
                k = 1
            #print("Current list:", h)
        hl.append(i)
    #print("Final list:", hl)
    return hl

def intersects(hl):
    for i in hl:
        for j in hl:
            if i.intersects(j) and i != j:
               return True
    return False

def intersects_percentage(r1, r2):
    r1a = r1.get_area()
    r1.intersect(r2)
    per1 = r1.get_area()/r1a
    per2 = r1.get_area()/r2.get_area()
    return per1, per2

def get_highlighted_text(page, highlights):
    all_words = page.get_text_words()
    # List to store all the highlighted texts
    highlight_text = []
    for r,c in highlights:
        sentence = [w[4] for w in all_words if intersects_percentage(fitz.Rect(w[0:4]),r)[0] > 0.1]
        if c['stroke'] == (0.0, 1.0, 1.0):
            highlight_text.append(" ".join(sentence) + " #hmm")
        else:
            highlight_text.append(" ".join(sentence))
    return highlight_text

file = input("Introduce filename:")
doc = fitz.open(file)

for i in range(len(doc)):
    page = doc[i]
    page = ink2highlight(page)
    doc.save("highlights" + file)

    highlights = find_highlights(page)
    highlight_text = get_highlighted_text(page, highlights)
    highlight_text = " ".join(highlight_text)
    print(highlight_text)