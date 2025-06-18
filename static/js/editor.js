class SupabaseUploadAdapter {
  constructor(loader) {
    this.loader = loader;
  }

  async upload() {
    const file = await this.loader.file;
    const filename = `${crypto.randomUUID()}_${file.name}`;

    const { data, error } = await supabase.storage
      .from("media")
      .upload(filename, file);

    if (error) throw error;

    const { publicUrl } = supabase.storage
      .from("media")
      .getPublicUrl(filename).data;

    return {
      default: publicUrl, // CKEditor insère cette URL dans le HTML
    };
  }
}

function uploadPlugin(editor) {
  editor.plugins.get("FileRepository").createUploadAdapter = (loader) =>
    new SupabaseUploadAdapter(loader);
}

ClassicEditor.create(document.querySelector("#editor"), {
  extraPlugins: [uploadPlugin],
})
  .then((editor) => {
    document.getElementById("save").onclick = async () => {
      const html = editor.getData();
      const title = prompt("Titre ?");
      const article = {
        title,
        slug: title.toLowerCase().replaceAll(" ", "-"),
        html, // le HTML CKEditor
        content: {}, // ou le JSON CKEditor
        author: "moi", // facultatif si tu veux stocker ça
      };

      await fetch("http://127.0.0.1:8000/article", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(article),
      });

      alert("✅ Article créé !");
    };
  })
  .catch(console.error);
