%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
%#<p>The open items are as follows: </p>
<div class="background">
  <h1 class="p">Todo List</h1>
  <table class="table">

%if len (rows) == 0:
 <h4 class = empty> the project is empty</h4>
%end



  %for row in rows:
    <tr class="select">
      %for col in row:
        <td class="p padding">{{col}}</td>
        
      %end
      <td class="padding"><svg onclick="window.location.href='/edit/{{row[0]}}'" class="trash_icon" t="1686370609630"" viewBox="0 0 1024 1024" p-id="7241"><path class="fill" d="M932.571429 882.285714H91.428571c-20.228571 0-36.571429 16.342857-36.571428 36.571429v41.142857c0 5.028571 4.114286 9.142857 9.142857 9.142857h896c5.028571 0 9.142857-4.114286 9.142857-9.142857v-41.142857c0-20.228571-16.342857-36.571429-36.571428-36.571429z m-711.2-96c2.285714 0 4.571429-0.228571 6.857142-0.571428L420.457143 752c2.285714-0.457143 4.457143-1.485714 6.057143-3.2l484.457143-484.457143a11.382857 11.382857 0 0 0 0-16.114286L721.028571 58.171429c-2.171429-2.171429-5.028571-3.314286-8.114285-3.314286s-5.942857 1.142857-8.114286 3.314286L220.342857 542.628571c-1.714286 1.714286-2.742857 3.771429-3.2 6.057143l-33.714286 192.228572a38.285714 38.285714 0 0 0 10.742858 34.057143c7.542857 7.314286 17.028571 11.314286 27.2 11.314285z" p-id="7242"></path></svg></td>
      <td class="padding"><svg onclick="window.location.href='/delete/{{row[0]}}'" class="trash_icon" t="1686369130017" viewBox="0 0 1024 1024" version="1.1" p-id="3437" data-spm-anchor-id="a313x.7781069.0.i2"><path d="M896 352l-73.792 556.608A96 96 0 0 1 727.04 992H296.96a96 96 0 0 1-95.168-83.392L128 352h768zM528 32A80 80 0 0 1 608 112V128h288a64 64 0 1 1 0 128H128a64 64 0 1 1 0-128h320v-16A80 80 0 0 1 528 32z" p-id="3438" data-spm-anchor-id="a313x.7781069.0.i4" class="selected"></path></svg></td>
    </tr>
    
  %end
  </table>

  <button class="add_button" onclick="window.location.href='/new'">ADD ITEM</button>
  
</div>

<style type="text/css">
    body {
      position: fixed; 
      top: 30%; 
      left: 30%;
    }
    .p{
        color: white;
    }

    .background{
        background:#FF6666;
        padding: 20px;
        border-radius: 20px;
    }
    .background::after{
      content: "";
      position: absolute;
      top: -20;
      left: -20;
      width: 100%;
      height: 100%;
      background-color: rgba(0,0,0,0.1); 
      z-index:-1;
      border-radius: 20px;
    }
    .select{
        background:#FF7777;
        border-radius: 20px
        
    }
    .table{
        border-spacing: 0 10px;
    }
    .trash_icon{
        width: 30px;
        fill: white;
    }
    .trash_icon:hover{
       fill: #d3d3d3;
    }
    .padding{
        padding: 10px;
    }
    .add_button{
        background: #FF6666;
        padding:10px;
        border-color: white;
        appearance:none;
        border-style:solid;
        border-width: 2px;
        color:white;
    }
    .add_button:hover{
        background: #FF5555;
    }
    .empty{
      color: white;
    }
</style>