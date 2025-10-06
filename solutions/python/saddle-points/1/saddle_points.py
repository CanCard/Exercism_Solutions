def saddle_points(matrix):
    for i, row in enumerate(matrix):
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")
    
    # bu bölüm için zip ve enumerate bilgisine ihtiyacımız oldu.

    points = []  # bulduğumuz saddle pointleri buraya ekle
    col_mins = [min(col) for col in zip(*matrix)]  # her sütunun min değeri

    for satir, deger_listesi in enumerate(matrix):
        for sutun, deger in enumerate(deger_listesi):
            if deger == max(deger_listesi) and deger == col_mins[sutun]:
                points.append({"row": satir + 1, "column": sutun + 1})
    
    return points