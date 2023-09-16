def n(l1, l2, l3, n1, n2, n3):   #(자기 자신, 2번째 꺼, 3번쨰 꺼)
    if mouse_x <= 270:
        if len(l1) != 0:
            choise = n1
            step = 1
        else:
            change = n1
            if choise == n2:
                if len(l1) == 0:
                    l1.insert(len(l1), l2[-1])
                    del(l2[-1])
                elif l2[-1] > l1[-1]:
                    l1.insert(len(l1), l2[-1])
                    del(l2[-1])
            if choise == n3:
                if len(l1) == 0:
                    l1.insert(len(l1), l3[-1])
                    del(l3[-1])
                elif l3[-1] > l1[-1]:
                    l1.insert(len(l1), l3[-1])
                    del(l3[-1])
        step = 0
        choise = 0
        change = 0
        return(l1, l2, l3)