# Báo cáo cuối kì môn cô Minh

<details><summary>Segment tree implement</summary>

File `SegmentTree.h` chứa template class `SegmentTree` dùng để xây dựng cây phân đoạn. Cách dùng rất đơn giản như sau:

```cpp
vector<int> data_vector = {5, -8, 6, 12, -9};

int sum(int x,int y){ return x+y; }
SegmentTree<int> range_sum_queries(dataVector, 0, sum);
```

Chỉ cần chỉ rõ toán tử 2 ngôi và phần tử đơn vị của toán tử đó. Thao tác trên cây phân đoạn cũng rất đơn giản:
```cpp
/* query the range l to r, 0 based array indexing.*/
range_sum_queries.query(l, r);

/* update the element at index idx to new_value. */
range_sum_queries.update(i, new_value);
```

</details>

Thường thì repo sẽ bao gồm file `main.html` và `Main.mp4`, nhưng nó cần một số file khác để chạy hoàn hảo. Chẳng may bị thiếu hoặc bị lỗi do vài lí do nào đó, `main.html` có thể được render lại bằng cách chạy file `main.py` với `manim` và `manim-slides` package.

Để render ra file slide, đảm bảo máy tính đã cài đặt `python` và [`ffmpeg`](https://ffmpeg.org/download.html).

Chạy lệnh sau để cài đặt `manim` và `manim-slides` package:
```bash
pip install manim manim-slides
```
Nếu câu lệnh trên không chạy được, làm theo hướng dẫn cài đặt cho [manim](https://docs.manim.community/en/stable/installation.html) và [manim-slides](https://eertmans.be/manim-slides/quickstart.html).

Tiếp theo, chạy 2 lệnh sau:
```bash
manim main.py -qh
manim-slides convert Main main.html --open
```

Lần đầu có thể lâu (em thử rồi, được 25 phút), nhưng lần sau sẽ nhanh hơn.

Repo có chia nhỏ `main.py` thành các file nhỏ, có thể thay thế `Main` và `main.py` ở câu lệnh trên bằng tên file và tên class tương đương để giảm thời gian render.


Nếu vẫn không chạy được, mong cô đừng vội cho điểm thấp, email em là nguyenduchuy_t64@hus.edu.vn, còn Facebook là https://www.facebook.com/lunalovegood236
