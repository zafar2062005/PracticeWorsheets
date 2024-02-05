def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]


def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    """
    Perform the convolution operation by applying the kernel over the input image.

    Parameter(s):
    - 2D array (int): This is the image on which you have to apply the kernel/filter and perform convolution. 
    - 1D array (int): The first entry in this array is the width of the kernel and the remaining entries are the values of the kernel.

    Returns:
    - 2D array (int): This is the matrix that is obtained after performing convolution.
    """
   
    image_h = len(image)
    image_w = len(image)

    kernel_h = len(kernel)
    kernel_w = len(kernel)

    h = kernel_h//2
    w = kernel_w//2

    conv_img = init_matrix(len(image), len(image))

    for i in range( image_h):
       for j in range(image_w ):
           sum = 0
           for a in range(kernel_h):
             for b in range(kernel_w):
                if i+a < len(image) and j+b < len(image[0]):
                    sum += kernel[a][b] * image[i+a][j+b] 
           conv_img[i][j] = sum    

    return conv_img         

def main(filename: str) -> list[list[int]]:
    """
    The main driver function that will run the entire program. 
    It should extract the image and the kernel from the file and pass them to filter_image(...).

    Parameter(s):
    - file_name (.txt file): Path to a text file that contains the image (2D array) and the kernel (1D array).

    Returns:
    - 2D array (int): This is the matrix that is obtained after executing filter_image(...)
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Extract the rows and cols of the input image
    rows, cols = map(int, lines[0].split())
    # Extract the input image
    image = []
    for line in lines[1:rows+1]:
        row = list(map(int, line.split()))
        image.append(row)

    # Extract the kernel
    kernel_data =  list(map(int, lines[-1].split()))
    kernel_size = kernel_data[0]
    kernel_values = kernel_data[1:]
    kernel_main =  kernel_values[::-1] # 1D list containing kernel

    kernel = [kernel_main[i:i+kernel_size] for i in range(0, len(kernel_main), kernel_size)]
    
    # return  image, kernel
    # Initialize the variables, image and kernel.
    
    # Pass those variables to filter_image(...)
    return filter_image(image, kernel)
filename = 'Inputs/matrix01.txt'    
print(main(filename))    

   

