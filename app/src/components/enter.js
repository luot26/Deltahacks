function getInput(){
    <form onSubmit={this.handleSubmit} method="post">
    <input type="text" placeholder="Enter your message" required />
    <button type="submit">Send</button>
</form>
}

export default getInput;
