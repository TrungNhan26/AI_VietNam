import numpy as np
import cv2

# Đọc và resize ảnh nền 1
bg1_image = cv2.imread('home.jpg', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

# Đọc và resize ảnh đối tượng
ob_image = cv2.imread('me_and_home.jpg', 1)
ob_image = cv2.resize(ob_image, (678, 381))

# Đọc và resize ảnh nền 2
bg2_image = cv2.imread('another_place.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))

def compute_difference(bg_img, input_img):
    # Tính sự khác biệt giữa ảnh nền và ảnh đầu vào
    difference_single_channel = cv2.absdiff(bg_img, input_img)

    # Chuyển đổi ảnh khác biệt sang màu xám
    difference_single_channel_gray = cv2.cvtColor(difference_single_channel, cv2.COLOR_BGR2GRAY)

    return difference_single_channel_gray

def compute_binary_mask(difference_single_channel):
    # Áp dụng ngưỡng để tạo mặt nạ nhị phân
    _, difference_binary = cv2.threshold(difference_single_channel, 30, 255, cv2.THRESH_BINARY)

    return difference_binary

def replace_background(bg1_image, bg2_image, ob_image):
    # Tính sự khác biệt giữa ảnh nền và ảnh đối tượng
    difference_single_channel = compute_difference(bg1_image, ob_image)

    # Tạo mặt nạ nhị phân
    binary_mask = compute_binary_mask(difference_single_channel)

    # Thay thế nền
    output = np.where(binary_mask[:, :, None] == 255, ob_image, bg2_image)

    return output

# Thay thế nền và hiển thị kết quả
a = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('Output', a)

# Chờ cho đến khi người dùng nhấn phím để đóng cửa sổ hiển thị
cv2.waitKey(0)
cv2.destroyAllWindows()
