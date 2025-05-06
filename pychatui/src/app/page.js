import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col h-screen p-4 sm:p-6 font-[family-name:var(--font-geist-sans)]">
      {/* Header */}
      <header className="flex items-center justify-center mb-4">
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="Next.js logo"
          width={120}
          height={30}
          priority
        />
      </header>

      {/* Chat messages container */}
      <main className="flex-1 overflow-y-auto flex flex-col gap-4 px-2 sm:px-4">
        {/* Example chat messages */}
        <div className="self-start max-w-[80%] bg-gray-200 dark:bg-gray-700 text-black dark:text-white px-4 py-2 rounded-xl">
          Hello! How can I help you today?
        </div>
        <div className="self-end max-w-[80%] bg-blue-500 text-white px-4 py-2 rounded-xl">
          I need some help with Next.js.
        </div>
        {/* Add more message bubbles here as needed */}
      </main>

      {/* Input box */}
      <footer className="mt-4 border-t border-gray-300 pt-2">
        <form className="flex items-center gap-2">
          <input
            type="text"
            placeholder="Type your message..."
            className="flex-1 px-4 py-2 rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-black dark:text-white focus:outline-none"
          />
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-full hover:bg-blue-700"
          >
            Send
          </button>
        </form>
      </footer>
    </div>
  );
}
