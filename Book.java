public class Book 
{
    private String name;
    private String isbn;
    private String author;
    private String publisher;
    public Book(String name, String isbn, String author, String publisher) 
    {
        this.name = name;
        this.isbn = isbn;
        this.author = author;
        this.publisher = publisher;
    }
    public void setName(String name)
    {
        this.name = name;
    }
    public void setIsbn(String isbn) 
    {
        this.isbn = isbn;
    }
    public void setAuthor(String author) 
    {
        this.author = author;
    }
    public void setPublisher(String publisher) 
    {
        this.publisher = publisher;
    }
    public String getName() 
    {
        return name;
    }
    public String getIsbn() 
    {
        return isbn;
    }
    public String getAuthor() 
    {
        return author;
    }
    public String getPublisher() 
    {
        return publisher;
    }
    public String getBookInfo() 
    {
        return "Book Name: " + name + ", ISBN: " + isbn + ", Author: " + author + ", Publisher: " + publisher;
    }
}
