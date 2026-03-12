
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from .radar import pulseRadar
from .target import pontualTarget

class Scene:
    def __init__(self, name):
        self.name = name
        self.targets = [pontualTarget(name="Target1", x=0, y=1000, velocity=100)]
        self.radar = pulseRadar(x=100, y=0, orientation=90, pulse_length=1.0, pulse_interval=10.0, amplitude=1.0)

    def plot(self):
        """Draw the current configuration of radar and targets on a static figure.

        This method creates and stores a matplotlib ``Figure`` and ``Axes``
        so that ``animate`` can reuse the same axes.  It also shows the plot
        immediately so that calling code can inspect the initial state.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(-500, 1500)
        ax.set_ylim(-500, 1500)
        ax.set_title(self.name)
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        ax.grid()

        # plot the radar and targets once
        ax.plot(self.radar.x, self.radar.y, 'ro', label='Radar')
        for target in self.targets:
            ax.plot(target.x, target.y, 'bx', label=target.name)
        ax.legend()

        # keep references for animation
        self.fig = fig
        self.ax = ax

        plt.show()

    def _init_animation(self):
        """Helper used by :py:meth:`animate` to initialise each frame."""
        # nothing to initialise beyond clearing axes; this is required by
        # FuncAnimation when blit=True but we don't use blit here.
        self.ax.clear()
        self.ax.set_xlim(-500, 1500)
        self.ax.set_ylim(-500, 1500)
        self.ax.set_title(self.name)
        self.ax.set_xlabel("X (m)")
        self.ax.set_ylabel("Y (m)")
        self.ax.grid()
        return []

    def _update_frame(self, frame):
        # advance target positions first
        self.update_targets()

        # clear and redraw everything on stored axes
        self.ax.clear()
        self.ax.set_xlim(-500, 1500)
        self.ax.set_ylim(-500, 1500)
        self.ax.set_title(self.name)
        self.ax.set_xlabel("X (m)")
        self.ax.set_ylabel("Y (m)")
        self.ax.grid()

        # plot the radar and targets
        self.ax.plot(self.radar.x, self.radar.y, 'ro', label='Radar')
        for target in self.targets:
            self.ax.plot(target.x, target.y, 'bx', label=target.name)
        self.ax.legend()

        # return the line artists for FuncAnimation
        return self.ax.lines

    def update_targets(self):
        for target in self.targets:
            # convert pulse interval (ms) to seconds when updating using
            # velocity in metres/second
            target.y += target.velocity * (self.radar.pulse_interval / 1000.0)

    def animate(self, frames=100, interval=None):
        """Animate the scene for a given number of frames.

        Parameters
        ----------
        frames : int
            Number of frames in the animation.
        interval : float | None
            Delay between frames in milliseconds.  Defaults to the radar's
            pulse interval if not provided.

        The animation displays a moving target and radar on a simple 2‑D
        plot.  ``plt.show()`` is called so that the figure window appears when
        this method is called from a script.
        """
        if not hasattr(self, 'fig') or not hasattr(self, 'ax'):
            # create figure/axes if plot() hasn't been called yet
            self.fig, self.ax = plt.subplots()

        if interval is None:
            interval = self.radar.pulse_interval

        anim = animation.FuncAnimation(
            self.fig,
            self._update_frame,
            init_func=self._init_animation,
            frames=frames,
            interval=interval,
            blit=False,
        )

        # keep a reference alive on the instance so that the animation
        # isn't garbage-collected as soon as this method returns
        self._anim = anim

        plt.show()
        return anim
