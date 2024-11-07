def hanoi(n, sumber, tujuan, bantu):
    if n == 1:
        # Jika hanya ada satu piringan, pindahkan langsung dari sumber ke tujuan
        print(f"Pindahkan piringan 1 dari {sumber} ke {tujuan}")
    else:
        # Langkah 1: Pindahkan n-1 piringan dari sumber ke bantu
        hanoi(n-1, sumber, bantu, tujuan)
        
        # Langkah 2: Pindahkan piringan terbesar ke-n dari sumber ke tujuan
        print(f"Pindahkan piringan {n} dari {sumber} ke {tujuan}")
        
        # Langkah 3: Pindahkan n-1 piringan dari bantu ke tujuan
        hanoi(n-1, bantu, tujuan, sumber)

# Memanggil fungsi dengan 4 piringan dari tiang A ke C menggunakan tiang B sebagai bantu
hanoi(4, 'A', 'C', 'B')
