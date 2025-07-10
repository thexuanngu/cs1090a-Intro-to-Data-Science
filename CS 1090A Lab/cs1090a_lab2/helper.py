import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import time

def rand_scaler():
    '''
    Return a random number between 2 and 5 in steps of 0.5
    '''
    return np.random.choice(np.arange(2,5.5,0.5)) 

def test_answer(answer, scaler):
    '''
    Compare guessed scaling factor to the truth and report results
    '''
    if answer == scaler:
        print(f'Correct! {scaler:g}x 🏆')
    else:
        print(f'Oops! The correct answer is: {scaler:g}x 😵')


# helper functions for tidying up our plots
def hide_spines(ax, ticks=False):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
def hide_ticks(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    
def hide_spines_n_ticks(ax):
    hide_spines(ax)
    hide_ticks(ax)

def label_choices(axs):
    fontdict = {'size': 20, 'weight': 'bold'}
    axs[0].set_xlabel('A', fontdict=fontdict)
    axs[1].set_xlabel('B', fontdict=fontdict)


# Random Visual Variation Functions
# def guess_length():
#     scaler = rand_scaler()
#     ax = sns.barplot(x=[1,scaler], y=['A','B'], color='lightblue', orient='h')
#     ax.set_title(r'How Much $\bf{Longer}$ is $\bf{B}$ than $\bf{A}$?')
#     ax.set(xticks=[])
#     hide_spines(ax)
#     return scaler

def guess_length():
    scaler = rand_scaler()
    
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Bar heights
    heights = [1, scaler]
    
    # Bar names
    bars = ['A', 'B']
    
    # Create bar plot
    ax.barh(bars, heights, color='lightblue')
    
    # Remove spines
    hide_spines_n_ticks(ax)
    
    # Set title
    ax.set_title(r'How Much $\bf{Longer}$ is $\bf{B}$ than $\bf{A}$?', fontsize=14, pad=15)
    
    return scaler

def guess_slope():
    fig, axs = plt.subplots(1,2, figsize=(8,4), sharex=True, sharey=True)
    x_lin = np.linspace(0,10,1000)
    m1 = np.random.uniform(0.25,1)
    scaler = rand_scaler()
    m2 = scaler*m1
    axs[0].plot(x_lin, m1*x_lin, lw=5)
    axs[1].plot(x_lin, m2*x_lin, lw=5)
    label_choices(axs)
    for ax in axs:
        hide_spines_n_ticks(ax)
    fig.suptitle(r'How Much of a Steeper Slope is $B$ than $A$?');
    plt.tight_layout()
    return scaler
    
def guess_area():
    fig, axs = plt.subplots(1,2, figsize=(8,4), sharex=True, sharey=True)
    plt.axis([0, 10, 0, 10])
    a1 = 5
    scaler = rand_scaler()
    a2 = scaler * a1
    c1 = plt.Circle((5, 5), radius=np.sqrt(a1/np.pi))
    c2 = plt.Circle((5, 5), radius=np.sqrt(a2/np.pi))
    axs[0].add_artist(c1)
    axs[1].add_artist(c2)
    label_choices(axs)
    for ax in axs:
        hide_spines_n_ticks(ax)
    plt.tight_layout()
    fig.suptitle(r"How Much Larger is $B$'s Area than $A$'s?")
    return scaler
    
def guess_darkness():
    fig, axs = plt.subplots(1,2, figsize=(8,4), sharex=True, sharey=True)
    plt.axis([0, 10, 0, 10])
    scaler = rand_scaler()
    darkness = 0.1
    c1 = plt.Circle((5, 5), radius=4, color=str(1-darkness))
    c2 = plt.Circle((5, 5), radius=4, color=str(1-scaler*darkness))
    axs[0].add_artist(c1)
    axs[1].add_artist(c2)
    label_choices(axs)
    for ax in axs:
        hide_spines_n_ticks(ax)
    plt.tight_layout()
    fig.suptitle(r"How Much $\bf{Darker}$ is $\bf{B}$ than $\bf{A}$?")
    return scaler
    
def show_color_gradient():
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, ax = plt.subplots(1,1,figsize=(10,1))
    ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap('RdYlBu'));
    ax.set_title('Color Map for Demonstration')
    ax.set_axis_off()
    
def guess_hue():
    fig = plt.figure(constrained_layout=False, figsize=(8, 4))
    spec = fig.add_gridspec(6, 2)
    ax1 = fig.add_subplot(spec[:5, 0])
    ax2 = fig.add_subplot(spec[:5, 1])
    # ax3 = fig.add_subplot(spec[5, :])
    for ax in [ax1, ax2]:
        hide_spines_n_ticks(ax)
    ax1.axis([0, 10, 0, 10])
    ax2.axis([0, 10, 0, 10])
    # ax3.axis([0, 255, 0, 1])
    scaler = rand_scaler()
    cm = matplotlib.cm.RdYlBu
    c = np.random.uniform(0,50/255)
    c1 = plt.Circle((5, 5), radius=4, color=cm(c))
    c2 = plt.Circle((5, 5), radius=4, color=cm(scaler*c))
    ax1.add_artist(c1)
    ax2.add_artist(c2)
    label_choices([ax1, ax2])
    plt.tight_layout()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    # ax3.imshow(gradient, aspect='auto', cmap=plt.get_cmap('RdYlBu'))
    # ax3.set_yticks([])

    fig.suptitle(r"How Much $\bf{Larger}$ is $\bf{B}$'s value than $\bf{A}$'s?"+\
                 "\n(just try and guess without reverting to comparing lengths!)", y=1.025)
    return scaler
