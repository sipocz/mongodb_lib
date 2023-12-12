# Create the figure and axes objects, specify the size and the dots per inches

def grafikon(df,col_1,desc_1,col_2="",desc_2="",n_graf=1,c_1=None, c_2=None,x=None,x_label="",title=None, title_2=None):
    __DEBUG__=False
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(14,7), dpi = 92)
    # Plot lines
    # Colors
    _upperline_color_="#8888aa"
    _text_color_="#111111"
    
    if c_1==None:
        _line1_color_="#FF9130"
    else:
        _line1_color_=c_1
    if c_2==None:
        _line2_color_="#716F81"
    else:
        _line2_color_=c_2

    # end of Colors

    if type(df)==list:
        # if df is a one dimension list
        if __DEBUG__:
            print(type(df))
        x_data=[i for i in range(len(df))]
        y_data=df
    else:
        # or df is a DataFrame
        y_data = df[col_1]
    
    if x!=None:
        x_data=df[x]
    else:
        if type(df)!=list:
            x_data = df.index
    
    
    if n_graf==1:
        _ = ax.plot(x_data, y_data, label=desc_1,c=_line1_color_)
        y_label=desc_1

    if n_graf==2:
        y2_data=df[col_2]
        _ = ax.plot(x_data, y_data, label=desc_1,c=_line1_color_)
        _ = ax.plot(x_data, y2_data, label=desc_2,c=_line2_color_)
        y_label=desc_1+" & "+desc_2
    ax.set_xlabel(x_label, fontsize=12, labelpad=10) # No need for an axis label
    ax.xaxis.set_label_position("bottom")
    ax.legend(loc="best", fontsize=8)
    
    
        
    

    ax.set_ylabel(y_label, fontsize=12, labelpad=10)
    ax.spines[['top','right']].set_visible(False)
    ax.plot([0.05, .9], [.98, .98], transform=fig.transFigure, clip_on=False, color=_upperline_color_, linewidth=1.6)
    ax.add_patch(plt.Rectangle((0.86,.98), 0.04, -0.02, facecolor=_upperline_color_, transform=fig.transFigure, clip_on=False, linewidth = 0))
    ax.text(x=0.05, y=.93, s=title, transform=fig.transFigure, ha='left', fontsize=14, weight='bold', alpha=.8, color=_text_color_)
    ax.text(x=0.05, y=.90, s=title_2, transform=fig.transFigure, ha='left', fontsize=12, alpha=.8, color=_text_color_)
    return(plt)


if __name__=="__main__":
    import pandas as pd    
    
    
    df=pd.DataFrame(data={"x":[1,2,3,4,5,6],"y":[22,33,44,55,66,77]})
    
 
    plt1=grafikon(df,"y","y_desc", "x","x_desc",n_graf=2,x="x",x_label="x", title="Hallo World", title_2="teszt_1")

    li=[99,45,32,12,39]
    plt2=grafikon(li,"y","y_desc",x_label="xdata")
    plt1.show()
    plt2.show()