import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image


def plot(
    image_list=[],
    figsize=(4, 8),
    nrows=2,
    ncols=4,
    ylabels=[],
    xlabels=[],
    axes_pad=0.05,
    save_path="grid_image.pdf",
):
    # * read images
    images = [Image.open(pth) for pth in image_list]
    # * create figure with shape and size
    fig = plt.figure(figsize=figsize)

    grid = ImageGrid(
        fig,
        111,  # similar to subplot(111)
        nrows_ncols=(nrows, ncols),  # creates 2x2 grid of axes
        axes_pad=axes_pad,  # pad between axes in inch.
    )

    ylab, xlab = 0, 0
    for idx, (ax, im) in enumerate(zip(grid, images)):
        # * remove axis line
        for key in ["right", "top", "left", "bottom"]:
            ax.spines[key].set_visible(False)

        # * remove ticks
        ax.set_xticks([])
        ax.set_yticks([])

        # * add label
        ax.set_ylabel(ylabels[ylab // ncols])
        ylab += 1

        ax.set_xlabel(xlabels[xlab % ncols])
        xlab += 1

        ax.imshow(im.resize(images[idx // ncols].size))

    plt.savefig(save_path, bbox_inches="tight")
    plt.show()
