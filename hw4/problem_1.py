def count_connected(voxel_grid):
    # TODO: Please write your code here
    if not voxel_grid:
        return 0

    X = len(voxel_grid)
    Y = len(voxel_grid[0])
    Z = len(voxel_grid[0][0])

    visited = set()

    def explore(x, y, z):
        if x < 0 or x >= X or y < 0 or y >= Y or z < 0 or z >= Z:
            return
        if voxel_grid[x][y][z] == 0:
            return
        if (x, y, z) in visited:
            return

        visited.add((x, y, z))

        explore(x+1, y, z)
        explore(x-1, y, z)
        explore(x, y+1, z)
        explore(x, y-1, z)
        explore(x, y, z+1)
        explore(x, y, z-1)

    components = 0

    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                if voxel_grid[x][y][z] == 1 and (x, y, z) not in visited:
                    components += 1
                    explore(x, y, z)

    return components


def visualise(voxel_grid):
    """
    This is a given method for visualising a provided voxel-grid.
    You can not change this function.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(np.array(voxel_grid))
    plt.show()


def main():
    # multidimensional representation of a single voxel.
    single_cube = [
        [
            [1]
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(single_cube)
    print(count_connected(single_cube))  # Should print the integer "1"

    # multidimensional representation of two cube-like components.
    two_cube_like_components = [
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(two_cube_like_components)
    print(count_connected(two_cube_like_components))  # Should print the integer "2"

    # multidimensional representation of 6 bars in diagonal.
    six_bars = [
        [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(six_bars)
    print(count_connected(six_bars))  # Should print the integer "6"

    # multidimensional representation of 3 connected blocks.
    connected_blocks = [
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(connected_blocks)
    print(count_connected(connected_blocks))  # Should print the integer "1"

    # multidimensional representation of 2 bars.
    two_bars = [
        [
            [1, 0],
        ], [
            [0, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(two_bars)
    print(count_connected(two_bars))  # Should print the integer "2"

    # multidimensional representation of 2 bars (2).
    two_bars_2 = [
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(two_bars_2)
    print(count_connected(two_bars_2))  # Should print the integer "2"

    # multidimensional representation of 3 connected componentes.
    connected_3 = [
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(connected_3)
    print(count_connected(connected_3))  # Should print the integer "3"

    # multidimensional representation of a partial wireframe.
    partial_wireframe = [
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(partial_wireframe)
    print(count_connected(partial_wireframe))  # Should print the integer "1"


if __name__ == "__main__":
    main()
