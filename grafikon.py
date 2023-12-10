# Create the figure and axes objects, specify the size and the dots per inches

def grafikon(fx,desc1,txt1,desc2="",txt2="",ngraf=1,c1=None, c2=None,x=None,xlabel="",title=None, title2=None):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(14,7), dpi = 92)
    # Plot lines
    _upperline_color_="#8888aa"
    _text_color_="#111111"
    if c1==None:
        _line1_color_="#FF9130"
    else:
        _line1_color_=c1
    if c2==None:
        _line2_color_="#716F81"
    else:
        _line2_color_=c2
    y_data = fx[desc1]
    x_data = fx.index
    if type(fx)==list:
        x_data=[i for i in range(len(fx))]
        y_data=fx

    if ngraf==1:
        line = ax.plot(x_data, y_data, label=txt1,c=_line1_color_)

    if ngraf==2:
        y2_data=fx[desc2]
        line1 = ax.plot(x_data, y_data, label=txt1,c=_line1_color_)
        line2 = ax.plot(x_data, y2_data, label=txt2,c=_line2_color_)

    ax.set_xlabel(xlabel, fontsize=12, labelpad=10) # No need for an axis label
    ax.xaxis.set_label_position("bottom")
    ax.legend(loc="best", fontsize=8)
    if ngraf==1:
        y_label=txt1
    if ngraf==2 and len(txt2)>0:
        y_label=txt1+" & "+txt2

    ax.set_ylabel(y_label, fontsize=12, labelpad=10)
    ax.spines[['top','right']].set_visible(False)
    ax.plot([0.05, .9], [.98, .98], transform=fig.transFigure, clip_on=False, color=_upperline_color_, linewidth=1.6)
    ax.add_patch(plt.Rectangle((0.86,.98), 0.04, -0.02, facecolor=_upperline_color_, transform=fig.transFigure, clip_on=False, linewidth = 0))
    ax.text(x=0.05, y=.93, s=title, transform=fig.transFigure, ha='left', fontsize=14, weight='bold', alpha=.8, color=_text_color_)
    ax.text(x=0.05, y=.90, s=title2, transform=fig.transFigure, ha='left', fontsize=12, alpha=.8, color=_text_color_)

if __name__=="__main__":
    import pandas as pd    
    print("Hello")
    
    df=pd.DataFrame(data={"x":[1,2,3,4,5,6],"y":[22,33,44,55,66,77]})
    df
    df.head()
    grafikon(df,"y","y",x="x")